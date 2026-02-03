# Support Forge Incident Knowledge Base

## Incident: SSL Certificate Propagation Delay (2026-01-27)

### Summary
After deploying Support Forge to Google Cloud Run and setting up domain mapping, the site was unreachable via HTTPS for approximately 20 minutes due to SSL certificate propagation delay.

### Timeline
- **22:08:09 UTC**: Domain mapping created for support-forge.com
- **22:19:26 UTC**: Certificate provisioned (CertificateProvisioned: True)
- **22:24:xx UTC**: Site still showing SSL handshake failures
- **22:27:xx UTC**: SSL working, site accessible

### Symptoms
- `curl: (35) schannel: failed to receive handshake, SSL/TLS connection failed`
- `openssl s_client` showed: "no peer certificate available"
- HTTP redirect (port 80) worked, but HTTPS (port 443) failed
- Cloud Run service showed Ready: True, CertificateProvisioned: True

### Root Cause
Google Cloud Run's managed SSL certificates take **15-30 minutes** to propagate across their global edge network after provisioning. The status shows "CertificateProvisioned: True" before propagation is complete.

### Diagnostic Commands
```bash
# Check Cloud Run service status
gcloud run services describe support-forge --region=us-central1 --format="table(status.conditions.type,status.conditions.status)"

# Check domain mapping status
gcloud beta run domain-mappings describe --domain=support-forge.com --region=us-central1

# Test direct Cloud Run URL (bypasses domain/SSL)
curl -sI https://support-forge-lr2jeeijaq-uc.a.run.app

# Test SSL certificate
openssl s_client -connect support-forge.com:443 -servername support-forge.com

# Check DNS resolution
nslookup support-forge.com
```

### Resolution
**Wait 15-30 minutes** after domain mapping creation for SSL to fully propagate.

### Workaround
While waiting for SSL propagation, the site is accessible via the direct Cloud Run URL:
- https://support-forge-lr2jeeijaq-uc.a.run.app

---

## Support Forge Architecture Reference

### Primary Stack (Google Cloud)
- **Service**: Cloud Run (support-forge)
- **Region**: us-central1
- **URL**: https://support-forge-lr2jeeijaq-uc.a.run.app
- **Database**: Cloud SQL PostgreSQL
- **Scaling**: 0-20 instances, auto-scale

### DNS (GoDaddy)
- **Domain**: support-forge.com
- **A Records**: 216.239.32.21, 216.239.34.21, 216.239.36.21, 216.239.38.21

### Backup Stack (AWS)
- **Service**: EC2 Docker
- **IP**: {LEGACY_EC2_IP} (Elastic IP)
- **SSH**: `~/.ssh/support-forge-key.pem`, user `ubuntu`
- **AWS Profile**: support-forge

### Failover Process
1. SSH to AWS EC2: `ssh -i ~/.ssh/support-forge-key.pem ubuntu@{LEGACY_EC2_IP}`
2. Pull latest code and deploy
3. Update GoDaddy A record to {LEGACY_EC2_IP}
4. Wait for DNS propagation (5-30 minutes)

---

## Key Learnings

1. **SSL Propagation**: Always expect 15-30 min delay after new Cloud Run domain mappings
2. **Status ≠ Ready**: "CertificateProvisioned: True" doesn't mean globally available
3. **Direct URL Fallback**: Cloud Run's direct URL always works for testing
4. **DNS TTL**: Keep TTL low (300s) for faster failover capability
