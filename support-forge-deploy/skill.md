# Support Forge Deployment Skill

Deploy Support Forge to production EC2 instance.

## Trigger
Use when Perry says: "deploy support forge", "push to production", "deploy sf", or similar.

## Pre-flight Checks
Before deploying, verify:
1. Working directory is `C:/Users/Jakeb/support-forge-app/`
2. Git status is clean (no uncommitted changes)
3. Current branch is `main`
4. `npm run build` succeeds locally

## Deployment Steps

### 1. Commit any pending changes
```bash
cd C:/Users/Jakeb/support-forge-app
git status
# If changes exist, commit them first
```

### 2. Push to GitHub
```bash
git push origin main
```

### 3. SSH and Deploy
```bash
ssh -i ~/.ssh/support-forge-key.pem ubuntu@44.197.15.102 << 'EOF'
cd /home/ubuntu/support-forge-app
git pull origin main
docker-compose build --no-cache web
docker-compose up -d
docker-compose logs --tail=50 web
EOF
```

### 4. Verify Deployment
- Check https://support-forge.com loads
- Test /api/health endpoint
- Monitor logs for errors

## Rollback Procedure
If deployment fails:
```bash
ssh -i ~/.ssh/support-forge-key.pem ubuntu@44.197.15.102 << 'EOF'
cd /home/ubuntu/support-forge-app
git log --oneline -5
git checkout HEAD~1
docker-compose build --no-cache web
docker-compose up -d
EOF
```

## Quick Restart (No Rebuild)
For config-only changes:
```bash
ssh -i ~/.ssh/support-forge-key.pem ubuntu@44.197.15.102 "cd /home/ubuntu/support-forge-app && docker-compose restart web"
```

## Post-Deploy Notifications
After successful deploy, optionally:
- Send Slack notification
- Update deployment log
- Clear CDN cache if applicable
