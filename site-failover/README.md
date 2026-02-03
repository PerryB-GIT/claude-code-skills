# Site Failover & Incident Response Skill

## Overview
Comprehensive toolkit for website incident response, failover procedures, and rollover between hosting providers.

## Invoke With
`/site-failover` or `/incident-response`

## Capabilities
- Diagnose site outages (DNS, SSL, server, application)
- Execute failover between GCP Cloud Run and AWS EC2
- Monitor SSL certificate propagation
- Automated health checks
- DNS management via GoDaddy
- Incident documentation and post-mortem

## Files
- `skill.md` - Main skill instructions
- `runbooks/` - Step-by-step procedures for common scenarios
- `diagnostics/` - Diagnostic scripts and commands

## Supported Sites
- support-forge.com (GCP Cloud Run + AWS EC2 backup)
- Extensible to other sites via configuration
