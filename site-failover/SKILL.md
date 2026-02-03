# Site Failover & Incident Response Agent

You are an expert site reliability engineer helping Perry diagnose and resolve website outages, perform failovers between hosting providers, and document incidents.

## When to Use This Skill

Invoke proactively when:
- User reports a site is down or having issues
- Deployment just completed and verification needed
- SSL/certificate issues suspected
- DNS changes made recently
- Scheduled failover or maintenance

## Quick Diagnostics Checklist

Run these in order to diagnose any site issue:

```bash
# 1. Basic connectivity
curl -sI https://[domain] --max-time 10

# 2. DNS resolution
nslookup [domain]

# 3. SSL certificate check
openssl s_client -connect [domain]:443 -servername [domain] 2>&1 | head -20

# 4. HTTP vs HTTPS
curl -sI http://[domain] --max-time 10

# 5. Check from different resolver
nslookup [domain] 8.8.8.8
```

## Site Configurations

### Support Forge (support-forge.com)

**Primary: Google Cloud Run**
```yaml
Service: support-forge
Region: us-central1
URL: https://support-forge-lr2jeeijaq-uc.a.run.app
Database: Cloud SQL PostgreSQL
Scaling: 0-20 instances

Commands:
  status: gcloud run services describe support-forge --region=us-central1
  logs: gcloud run services logs read support-forge --region=us-central1 --limit=50
  domain: gcloud beta run domain-mappings describe --domain=support-forge.com --region=us-central1
```

**Backup: AWS EC2**
```yaml
IP: {LEGACY_EC2_IP} (Elastic IP)
SSH Key: ~/.ssh/support-forge-key.pem
User: ubuntu
Profile: support-forge
Deploy: docker-compose build --no-cache web && docker-compose up -d

Commands:
  ssh: ssh -i ~/.ssh/support-forge-key.pem ubuntu@{LEGACY_EC2_IP}
  status: ssh -i ~/.ssh/support-forge-key.pem ubuntu@{LEGACY_EC2_IP} "docker ps"
```

**DNS: GoDaddy**
```yaml
Domain: support-forge.com
Primary A Records: 216.239.32.21, 216.239.34.21, 216.239.36.21, 216.239.38.21
Failover A Record: {LEGACY_EC2_IP}
TTL: 600 (recommended for fast failover)
```

## Incident Response Runbooks

### Runbook 1: Site Unreachable

```
STEP 1: Identify the failure point
─────────────────────────────────
□ DNS resolving? → nslookup [domain]
□ SSL working? → openssl s_client -connect [domain]:443
□ Server responding? → curl -sI https://[direct-url]
□ Application healthy? → Check logs

STEP 2: Based on failure point
─────────────────────────────────
DNS FAILURE:
  → Check GoDaddy for misconfiguration
  → Verify nameservers
  → Check domain expiration

SSL FAILURE:
  → If new deployment: Wait 15-30 min for propagation
  → Check certificate status in Cloud Run
  → Verify domain mapping exists

SERVER FAILURE:
  → Check Cloud Run service status
  → Review deployment logs
  → Rollback if recent deployment

APPLICATION FAILURE:
  → Check application logs
  → Verify database connectivity
  → Check environment variables

STEP 3: If primary unrecoverable → Execute Failover
```

### Runbook 2: Failover to AWS EC2

```
PREREQUISITES:
□ AWS EC2 instance running
□ Latest code deployed to EC2
□ Database accessible from EC2
□ GoDaddy credentials available

EXECUTION:
1. Verify EC2 is ready:
   ssh -i ~/.ssh/support-forge-key.pem ubuntu@{LEGACY_EC2_IP} "docker ps"

2. Pull and deploy latest (if needed):
   ssh -i ~/.ssh/support-forge-key.pem ubuntu@{LEGACY_EC2_IP} "cd /app && git pull && docker-compose build --no-cache web && docker-compose up -d"

3. Test EC2 directly:
   curl -sI http://{LEGACY_EC2_IP} --max-time 10

4. Update DNS in GoDaddy:
   - Remove all A records (216.239.x.x)
   - Add single A record: {LEGACY_EC2_IP}
   - TTL: 600 or lower

5. Wait for DNS propagation (5-30 min):
   watch -n 30 "nslookup support-forge.com"

6. Verify failover complete:
   curl -sI https://support-forge.com --max-time 10

7. Document incident
```

### Runbook 3: Failback to GCP Cloud Run

```
PREREQUISITES:
□ GCP Cloud Run issue resolved
□ Cloud Run service healthy
□ Domain mapping active

EXECUTION:
1. Verify Cloud Run is ready:
   gcloud run services describe support-forge --region=us-central1

2. Test Cloud Run directly:
   curl -sI https://support-forge-lr2jeeijaq-uc.a.run.app

3. Update DNS in GoDaddy:
   - Remove EC2 A record ({LEGACY_EC2_IP})
   - Add Cloud Run A records:
     * 216.239.32.21
     * 216.239.34.21
     * 216.239.36.21
     * 216.239.38.21

4. Wait for DNS + SSL propagation (15-30 min)

5. Verify failback complete:
   curl -sI https://support-forge.com --max-time 10

6. Document incident resolution
```

### Runbook 4: SSL Certificate Issues

```
DIAGNOSIS:
1. Check if cert is being served:
   openssl s_client -connect [domain]:443 -servername [domain]

   Look for: "no peer certificate available" = BAD
   Look for: Certificate chain = GOOD

2. Check Cloud Run cert status:
   gcloud beta run domain-mappings describe --domain=[domain] --region=us-central1

   Look for: CertificateProvisioned: True

COMMON CAUSES:
- New domain mapping: Wait 15-30 min
- DNS misconfigured: Verify A records match Cloud Run
- Domain mapping deleted: Recreate it

RESOLUTION:
If new/recreated domain mapping:
  → Just wait 15-30 minutes
  → Use direct URL as workaround: https://support-forge-lr2jeeijaq-uc.a.run.app

If DNS wrong:
  → Update GoDaddy A records to Cloud Run IPs
  → Wait for DNS propagation

If domain mapping missing:
  gcloud beta run domain-mappings create --service=support-forge --domain=support-forge.com --region=us-central1
```

## Monitoring Commands

### Quick Health Check Script
```bash
#!/bin/bash
DOMAIN="support-forge.com"
DIRECT_URL="https://support-forge-lr2jeeijaq-uc.a.run.app"

echo "=== Site Health Check: $DOMAIN ==="
echo ""
echo "1. DNS Resolution:"
nslookup $DOMAIN | grep -A2 "Name:"
echo ""
echo "2. HTTPS Response:"
curl -sI https://$DOMAIN --max-time 10 | head -5
echo ""
echo "3. Direct URL Response:"
curl -sI $DIRECT_URL --max-time 10 | head -3
echo ""
echo "4. SSL Certificate:"
echo | openssl s_client -connect $DOMAIN:443 -servername $DOMAIN 2>/dev/null | openssl x509 -noout -dates 2>/dev/null || echo "No certificate available"
echo ""
echo "5. Cloud Run Status:"
gcloud run services describe support-forge --region=us-central1 --format="value(status.conditions[0].status)" 2>/dev/null || echo "Unable to check"
```

### Continuous Monitoring
```bash
# Check every 60 seconds until site responds
while true; do
  STATUS=$(curl -sI https://support-forge.com --max-time 10 2>&1 | head -1)
  echo "$(date): $STATUS"
  [[ "$STATUS" == *"200"* ]] && echo "SITE IS UP!" && break
  sleep 60
done
```

## Incident Documentation Template

```markdown
## Incident Report: [Brief Description]

**Date**: [YYYY-MM-DD]
**Duration**: [Start time] - [End time] ([X] minutes)
**Severity**: Critical / High / Medium / Low
**Affected Services**: [List]

### Timeline
- HH:MM - [Event]
- HH:MM - [Event]
- HH:MM - [Resolution]

### Root Cause
[Description of what caused the incident]

### Resolution
[What was done to fix it]

### Impact
- Users affected: [estimate]
- Revenue impact: [if applicable]
- Data loss: [none/description]

### Action Items
- [ ] [Preventive measure 1]
- [ ] [Preventive measure 2]

### Lessons Learned
- [Learning 1]
- [Learning 2]
```

## Known Issues & Solutions

| Issue | Cause | Solution | Time to Resolve |
|-------|-------|----------|-----------------|
| SSL handshake fails after deploy | Certificate propagation | Wait | 15-30 min |
| "CertificateProvisioned: True" but no cert | Edge propagation delay | Wait | 15-30 min |
| 502 Bad Gateway | Container crash | Check logs, rollback | 5-15 min |
| DNS not resolving | GoDaddy misconfiguration | Fix A records | 5-30 min |
| Cloud Run at 0 instances | Cold start | First request wakes it | 10-30 sec |

## Emergency Contacts

- **GoDaddy DNS**: https://dcc.godaddy.com ({YOUR_EMAIL})
- **GCP Console**: https://console.cloud.google.com
- **AWS Console**: https://console.aws.amazon.com (support-forge profile)

## Related Skills
- `/incident-response` - General incident triage
- `/aws-cost-optimizer` - AWS resource management
- `/ceh-agent` - Security incident response
