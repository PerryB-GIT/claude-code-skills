# Client Site Deployment Skill

Quick deployment helper for Perry's client sites.

## Supported Sites

| Site | Type | Deploy Method |
|------|------|---------------|
| vineyardvalais.com | Next.js | Amplify (auto from git) |
| witchsbroomcleaning.com | Static | S3 + CloudFront |
| sweetmeadow-bakery.com | Next.js | Amplify (appId: dqa0p0t9xllsd) |
| homebasevet.com | Static | S3: homebasevet-staging |
| me.jbailes.com / jpbailes.com | Next.js | Amplify (appId: d373lws1f7wsen) |
| support-forge.com | Next.js | EC2 Docker (use /support-forge-deploy) |

## Amplify Sites (Auto-Deploy)
These auto-deploy on git push to main:
```bash
git add .
git commit -m "feat: update"
git push origin main
# Amplify triggers build automatically
```

Check status:
```bash
aws amplify list-jobs --app-id <APP_ID> --branch-name main --max-items 1
```

## Static S3 Sites

### witchsbroomcleaning.com
```bash
aws s3 sync ./dist s3://witchsbroomcleaning-site --delete
aws cloudfront create-invalidation --distribution-id <DIST_ID> --paths "/*"
```

### homebasevet.com
```bash
aws s3 sync ./build s3://homebasevet-staging --delete
```

## Verify Deployment
After any deploy:
1. Check the live URL loads
2. Hard refresh (Ctrl+Shift+R) to bust cache
3. Test key functionality (forms, links)
4. Check mobile responsiveness

## Rollback
For Amplify sites - redeploy previous commit:
```bash
aws amplify start-job --app-id <APP_ID> --branch-name main --job-type RELEASE --commit-id <PREVIOUS_COMMIT>
```

For S3 sites - restore from backup or redeploy previous build.
