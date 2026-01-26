# OSINT & Reconnaissance Skill

## Legal Notice
OSINT must be conducted ethically and legally. Only gather publicly available information. Do not access private accounts, bypass authentication, or violate terms of service.

## Domain Intelligence

### DNS & WHOIS
```bash
# WHOIS
whois target.com
whois -h whois.arin.net 1.2.3.4  # IP WHOIS

# DNS records
dig target.com ANY +noall +answer
dig target.com MX +short
dig target.com TXT +short
dig target.com NS +short
dig -x 1.2.3.4  # Reverse DNS

# DNS zone transfer (if misconfigured)
dig axfr @ns1.target.com target.com

# Historical DNS
# securitytrails.com
# dnsdumpster.com
```

### Subdomain Discovery
```bash
# Passive enumeration
subfinder -d target.com -all -silent
amass enum -passive -d target.com -o subs.txt
assetfinder --subs-only target.com

# Certificate transparency
curl -s "https://crt.sh/?q=%.target.com&output=json" | jq -r '.[].name_value' | sort -u

# DNS bruteforce (active)
gobuster dns -d target.com -w subdomains.txt
shuffledns -d target.com -w subdomains.txt -r resolvers.txt

# Verify alive
httpx -l subs.txt -silent -status-code -title
```

### Web Presence
```bash
# Technology stack
whatweb -v target.com
wappalyzer https://target.com
builtwith.com

# Wayback Machine
waybackurls target.com | sort -u
gau target.com  # GetAllURLs

# Web archives
# web.archive.org
# archive.today

# robots.txt & sitemap
curl -s https://target.com/robots.txt
curl -s https://target.com/sitemap.xml
```

## Person OSINT

### Username Enumeration
```bash
# Cross-platform username search
sherlock username
maigret username
whatsmyname.app

# Email verification
holehe email@target.com
```

### Social Media
```
# Manual searches
- LinkedIn: site:linkedin.com "John Smith" "Company"
- Twitter/X: from:username OR to:username
- Facebook: site:facebook.com "John Smith"
- Instagram: site:instagram.com "username"
- GitHub: user:username

# Tools
- socialscan (username availability)
- twint (Twitter scraping - deprecated, use API)
- instaloader (Instagram)
```

### Breach Data (Legal Sources)
```
# Public breach notification
- haveibeenpwned.com (email check)
- dehashed.com (requires account)
- intelx.io (intelligence search)
- breachdirectory.org

# DO NOT use stolen credentials
# Report findings responsibly
```

### People Search
```
# Public records (US)
- whitepages.com
- truepeoplesearch.com
- fastpeoplesearch.com
- voterrecords.com

# Professional
- LinkedIn
- Crunchbase
- RocketReach
```

## Company OSINT

### Business Intelligence
```
# Corporate records
- SEC EDGAR (public filings)
- OpenCorporates
- Crunchbase
- Glassdoor (employee reviews)

# News & press
- Google News
- PRNewswire
- BusinessWire

# Financial
- Yahoo Finance
- Bloomberg
- D&B Hoovers
```

### Technical Footprint
```bash
# IP ranges & ASN
whois -h whois.radb.net -- '-i origin AS12345'
bgp.he.net
ipinfo.io

# Shodan
shodan search org:"Company Name"
shodan search hostname:target.com
shodan search ssl.cert.subject.cn:target.com

# Censys
censys search services.http.response.html_title:"Company"

# BuiltWith
builtwith.com/target.com
```

### Employee Discovery
```bash
# LinkedIn enumeration
# Manual: site:linkedin.com "Company Name"
# Tools: linkedin2username, CrossLinked

# Email pattern discovery
hunter.io
clearbit.com
# Common patterns:
# firstname.lastname@company.com
# flastname@company.com
# firstnamel@company.com
```

## Infrastructure OSINT

### IP & Network
```bash
# IP geolocation
curl ipinfo.io/1.2.3.4
geoiplookup 1.2.3.4

# ASN lookup
whois -h whois.cymru.com " -v 1.2.3.4"

# BGP routing
bgp.he.net
bgpview.io

# Passive DNS
passivetotal.org
virustotal.com
```

### Cloud Resources
```bash
# S3 buckets
# bucket-finder
# cloud_enum
# Pattern: company-backup, company-dev, company-prod

# Azure blobs
# company.blob.core.windows.net

# GCP storage
# storage.googleapis.com/company-bucket
```

## Document & Metadata OSINT

### File Metadata
```bash
# Extract metadata
exiftool document.pdf
exiftool -a -u -g1 image.jpg

# FOCA (Windows)
# Metagoofil
metagoofil -d target.com -t pdf,doc,xls -l 100 -o output

# Google dorks for documents
# site:target.com filetype:pdf
# site:target.com filetype:xlsx
# site:target.com filetype:docx
```

### Google Dorks
```
# Sensitive files
site:target.com filetype:log
site:target.com filetype:sql
site:target.com filetype:env
site:target.com filetype:bak

# Directories
site:target.com intitle:"index of"
site:target.com inurl:/admin/
site:target.com inurl:/backup/

# Credentials
site:target.com intext:"password"
site:target.com ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf

# Error messages
site:target.com "sql syntax" | "mysql_fetch"
site:target.com "warning" "include" filetype:php
```

## Geolocation OSINT

### Image Geolocation
```bash
# EXIF GPS data
exiftool -gps* image.jpg

# Reverse image search
# Google Images
# TinEye
# Yandex Images (often better for faces)

# Geolocation tools
# Google Maps/Earth
# SunCalc (shadow analysis)
# Geoguessr techniques
```

### Physical Location
```
# Satellite imagery
- Google Earth Pro
- Bing Maps
- Yandex Maps
- Sentinel Hub (historical)

# Street view
- Google Street View
- Mapillary
- KartaView
```

## Threat Intelligence

### IOC Lookup
```bash
# VirusTotal
vt url https://suspicious.com
vt hash abc123...

# AbuseIPDB
curl -s "https://api.abuseipdb.com/api/v2/check?ipAddress=1.2.3.4" -H "Key: $API_KEY"

# OTX AlienVault
# URLhaus
# MalwareBazaar
# ThreatFox
```

### Dark Web (Tor - Legal monitoring only)
```
# Search engines
- Ahmia
- Torch
- DuckDuckGo .onion

# Monitoring services
- Flare
- SpyCloud
- Recorded Future
```

## OSINT Workflow

### Target Scoping
1. Define objectives (what do you need to find?)
2. Identify seed data (domain, name, email, username)
3. Choose appropriate tools
4. Document everything with timestamps
5. Verify findings from multiple sources

### Data Organization
```
osint_project/
├── target_info.md
├── domains/
│   ├── subdomains.txt
│   ├── dns_records.txt
│   └── whois.txt
├── people/
│   ├── employees.csv
│   └── social_media.md
├── infrastructure/
│   ├── ip_ranges.txt
│   └── technologies.md
├── documents/
│   └── metadata_findings.md
└── timeline.md
```

## Tools Summary

| Category | Tools |
|----------|-------|
| Subdomain | subfinder, amass, assetfinder |
| DNS | dig, host, dnsenum |
| Username | sherlock, maigret |
| Email | holehe, hunter.io |
| Web | waybackurls, gau, httpx |
| Network | shodan, censys, nmap |
| Documents | metagoofil, exiftool |
| All-in-one | recon-ng, spiderfoot, maltego |

## Resources
- OSINT Framework: https://osintframework.com
- IntelTechniques: https://inteltechniques.com
- Bellingcat guides: https://www.bellingcat.com/resources/
- SANS OSINT: https://www.sans.org/blog/-must-have-free-resources-for-open-source-intelligence-osint-/
