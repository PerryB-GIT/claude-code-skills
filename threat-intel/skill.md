# Threat Intelligence

## IOC Lookup Resources

### IP/Domain Reputation
| Service | URL | API |
|---------|-----|-----|
| VirusTotal | virustotal.com | Yes |
| AbuseIPDB | abuseipdb.com | Yes |
| Shodan | shodan.io | Yes |
| Censys | censys.io | Yes |
| GreyNoise | greynoise.io | Yes |
| OTX AlienVault | otx.alienvault.com | Yes |
| ThreatFox | threatfox.abuse.ch | Yes |

### File/Hash Analysis
| Service | URL |
|---------|-----|
| VirusTotal | virustotal.com |
| Hybrid Analysis | hybrid-analysis.com |
| Any.Run | any.run |
| Joe Sandbox | joesandbox.com |
| MalwareBazaar | bazaar.abuse.ch |
| Malshare | malshare.com |

### URL Analysis
| Service | URL |
|---------|-----|
| URLhaus | urlhaus.abuse.ch |
| URLScan | urlscan.io |
| PhishTank | phishtank.com |

## MITRE ATT&CK Framework

### Tactics (TA)
| ID | Tactic | Description |
|----|--------|-------------|
| TA0001 | Initial Access | Gaining entry |
| TA0002 | Execution | Running code |
| TA0003 | Persistence | Maintaining access |
| TA0004 | Privilege Escalation | Higher permissions |
| TA0005 | Defense Evasion | Avoiding detection |
| TA0006 | Credential Access | Stealing creds |
| TA0007 | Discovery | Learning environment |
| TA0008 | Lateral Movement | Moving around |
| TA0009 | Collection | Gathering data |
| TA0010 | Exfiltration | Stealing data |
| TA0011 | Command & Control | Communication |
| TA0040 | Impact | Damage/disruption |

### Common Techniques
```
# Initial Access
T1566 - Phishing
T1190 - Exploit Public-Facing App
T1133 - External Remote Services

# Execution
T1059 - Command and Scripting Interpreter
T1204 - User Execution

# Persistence
T1547 - Boot or Logon Autostart
T1053 - Scheduled Task/Job
T1136 - Create Account

# Privilege Escalation
T1548 - Abuse Elevation Control
T1068 - Exploitation for Privilege Escalation

# Defense Evasion
T1070 - Indicator Removal
T1036 - Masquerading
T1027 - Obfuscated Files

# Credential Access
T1003 - OS Credential Dumping
T1110 - Brute Force
T1555 - Credentials from Password Stores

# Lateral Movement
T1021 - Remote Services
T1570 - Lateral Tool Transfer
```

## Threat Actor Research

### APT Groups Database
- MITRE ATT&CK Groups: https://attack.mitre.org/groups/
- Malpedia: https://malpedia.caad.fkie.fraunhofer.de/
- ThaiCERT APT Encyclopedia
- ETDA Threat Actor Encyclopedia

### Common APT Groups
| Group | Aliases | Origin | Targets |
|-------|---------|--------|---------|
| APT28 | Fancy Bear | Russia | Government, Defense |
| APT29 | Cozy Bear | Russia | Government |
| APT41 | Winnti | China | Multiple sectors |
| Lazarus | Hidden Cobra | DPRK | Finance, Crypto |
| FIN7 | Carbanak | Russia | Finance, Retail |

## CVE Research

### Resources
```
# NVD (National Vulnerability Database)
https://nvd.nist.gov/

# CVE Details
https://www.cvedetails.com/

# Exploit-DB
https://www.exploit-db.com/

# CISA KEV (Known Exploited Vulnerabilities)
https://www.cisa.gov/known-exploited-vulnerabilities-catalog

# Vulners
https://vulners.com/
```

### CVSS Scoring
| Score | Severity |
|-------|----------|
| 0.0 | None |
| 0.1-3.9 | Low |
| 4.0-6.9 | Medium |
| 7.0-8.9 | High |
| 9.0-10.0 | Critical |

## Malware Analysis Workflow

### Static Analysis
```bash
# File info
file malware.exe
exiftool malware.exe

# Strings extraction
strings -n 8 malware.exe
floss malware.exe  # FLARE Obfuscated String Solver

# PE analysis
pefile malware.exe
pestudio malware.exe  # GUI

# Hash calculation
sha256sum malware.exe
md5sum malware.exe
ssdeep malware.exe  # Fuzzy hash
```

### Dynamic Analysis
```bash
# Sandbox execution
# Use isolated VM or cloud sandbox

# Process monitoring
procmon.exe  # Windows
strace ./malware  # Linux

# Network monitoring
Wireshark
FakeNet-NG
INetSim

# File system monitoring
Process Monitor
inotifywait
```

### Yara Rules
```yara
rule Suspicious_PowerShell {
    meta:
        description = "Detects suspicious PowerShell patterns"
        author = "Your Name"
        date = "2025-01"
    strings:
        $s1 = "IEX" nocase
        $s2 = "Invoke-Expression" nocase
        $s3 = "-enc" nocase
        $s4 = "FromBase64String" nocase
        $s5 = "DownloadString" nocase
    condition:
        2 of them
}
```

## Threat Intelligence Platforms

### Open Source
- MISP (Malware Information Sharing Platform)
- OpenCTI
- TheHive + Cortex
- YETI

### Commercial
- Recorded Future
- Mandiant Advantage
- CrowdStrike Falcon X
- Anomali ThreatStream

## Reporting Template

```markdown
# Threat Intelligence Report

## Executive Summary
[Brief overview for leadership]

## Threat Actor Profile
- **Name/Aliases**:
- **Attribution**:
- **Motivation**:
- **Target Industries**:
- **Geographic Focus**:

## TTPs (MITRE ATT&CK)
| Tactic | Technique | Description |
|--------|-----------|-------------|

## Indicators of Compromise
### Network
| Type | Value | Description |
|------|-------|-------------|
| IP | | |
| Domain | | |
| URL | | |

### File
| Hash (SHA256) | Filename | Description |
|---------------|----------|-------------|

### Host
| Type | Value | Description |
|------|-------|-------------|

## Detection Recommendations
### SIEM Rules
[Detection logic]

### Yara Rules
[Signatures]

### Network Signatures
[Snort/Suricata rules]

## Mitigation Recommendations
1. [Recommendation 1]
2. [Recommendation 2]

## References
- [Source 1]
- [Source 2]
```

## Feeds & Subscriptions

### Free Feeds
- AlienVault OTX
- Abuse.ch (URLhaus, MalwareBazaar, ThreatFox)
- CISA Alerts
- US-CERT
- Feodo Tracker
- EmergingThreats

### Government Resources
- CISA: https://www.cisa.gov/
- FBI IC3: https://www.ic3.gov/
- NSA Cybersecurity: https://www.nsa.gov/cybersecurity/
- NIST: https://www.nist.gov/cyberframework
