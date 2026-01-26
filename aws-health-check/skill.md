# AWS Health Check Skill

Quick health check across all of Perry's AWS resources.

## Profiles to Check
- `default` ({YOUR_AWS_ACCOUNT}) - Main account
- `support-forge` - Support Forge hosting
- `sweetmeadow` - Sweetmeadow resources

## Health Check Sequence

### 1. EC2 Instances
```bash
# Support Forge EC2
aws ec2 describe-instance-status --instance-ids <INSTANCE_ID> --profile support-forge

# Quick connectivity test
curl -s -o /dev/null -w "%{http_code}" https://support-forge.com/api/health
```

### 2. Amplify Apps Status
```bash
# List all apps
aws amplify list-apps --profile default

# Check recent builds
aws amplify list-jobs --app-id dqa0p0t9xllsd --branch-name main --max-items 3 --profile sweetmeadow
aws amplify list-jobs --app-id d373lws1f7wsen --branch-name main --max-items 3 --profile default
```

### 3. S3 Buckets
```bash
aws s3 ls --profile default | grep -E "(witchsbroom|homebase)"
```

### 4. CloudFront Distributions
```bash
aws cloudfront list-distributions --query "DistributionList.Items[*].{Id:Id,Domain:DomainName,Status:Status}" --profile default
```

### 5. Route53 / DNS (if using)
```bash
aws route53 list-hosted-zones --profile default
```

### 6. Cost Quick Check
```bash
aws ce get-cost-and-usage \
  --time-period Start=$(date -d '30 days ago' +%Y-%m-%d),End=$(date +%Y-%m-%d) \
  --granularity MONTHLY \
  --metrics BlendedCost \
  --profile default
```

## Output Format
Report status as:
- OK - Service healthy
- WARN - Degraded but functional
- ERROR - Down or failing

## Common Issues
- EC2 stopped unexpectedly - Check billing/limits
- Amplify build failed - Check build logs
- S3 403 errors - Check bucket policy
- CloudFront 5xx - Check origin health
