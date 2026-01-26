# Cybersecurity Incident Response

## NIST SP 800-61 Framework

### Phase 1: Preparation
- Incident response team contacts
- Communication channels (secure)
- Forensic tools ready
- Documentation templates
- Legal/compliance contacts
- Management escalation path

### Phase 2: Detection & Analysis

#### Initial Triage
```bash
# Severity classification
P1 - Critical: Active breach, data exfiltration, ransomware
P2 - High: Confirmed compromise, lateral movement
P3 - Medium: Suspicious activity, potential compromise
P4 - Low: Policy violation, minor security event

# Questions to answer
- What systems are affected?
- What's the scope of impact?
- Is the attack ongoing?
- What data may be compromised?
```

#### Windows Triage
```powershell
# Current connections
netstat -ano | findstr ESTABLISHED
Get-NetTCPConnection | Where-Object {$_.State -eq 'Established'}

# Running processes
tasklist /v
Get-Process | Select-Object Name, Id, Path, Company
wmic process get processid,parentprocessid,commandline

# Scheduled tasks
schtasks /query /fo LIST /v
Get-ScheduledTask | Where-Object {$_.State -eq 'Ready'}

# Services
sc query
Get-Service | Where-Object {$_.Status -eq 'Running'}

# Recent file modifications
forfiles /P C:\ /S /D +0 /C "cmd /c echo @path @fdate @ftime"
Get-ChildItem -Path C:\ -Recurse -File | Where-Object {$_.LastWriteTime -gt (Get-Date).AddDays(-1)}

# User accounts
net user
net localgroup administrators
Get-LocalUser
Get-LocalGroupMember -Group "Administrators"

# Event logs
wevtutil qe Security /c:50 /f:text /rd:true
Get-WinEvent -LogName Security -MaxEvents 100

# Persistence locations
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
```

#### Linux Triage
```bash
# Current connections
netstat -tulpn
ss -tulpn
lsof -i

# Running processes
ps auxf
pstree -p

# Cron jobs
crontab -l
cat /etc/crontab
ls -la /etc/cron.*

# User accounts
cat /etc/passwd
cat /etc/shadow  # if root
last -100
lastlog

# Recent modifications
find / -mtime -1 -type f 2>/dev/null
find / -ctime -1 -type f 2>/dev/null

# Auth logs
cat /var/log/auth.log | tail -100
journalctl -u sshd --since "1 hour ago"

# Persistence
cat /etc/rc.local
systemctl list-unit-files --state=enabled
ls -la ~/.bashrc ~/.profile /etc/profile.d/
```

#### Network Analysis
```bash
# Capture traffic
tcpdump -i eth0 -w capture.pcap
tcpdump -i eth0 host suspicious.ip

# Analyze with Wireshark filters
# Suspicious traffic patterns:
ip.addr == malicious.ip
http.request.uri contains "cmd"
dns.qry.name contains "malware"
tcp.flags.syn == 1 && tcp.flags.ack == 0

# Zeek/Bro logs
cat conn.log | zeek-cut id.orig_h id.resp_h id.resp_p
```

### Phase 3: Containment

#### Short-term Containment
```bash
# Network isolation
# Disable network adapter
# Move to isolated VLAN
# Block at firewall

# Windows - disable adapter
netsh interface set interface "Ethernet" disable

# Linux - bring down interface
ip link set eth0 down

# Block IP at firewall
# Windows
netsh advfirewall firewall add rule name="Block Attacker" dir=in action=block remoteip=X.X.X.X

# Linux (iptables)
iptables -A INPUT -s X.X.X.X -j DROP
```

#### Long-term Containment
```bash
# Credential reset
# Patch vulnerabilities
# Enhanced monitoring
# Segment compromised systems
```

### Phase 4: Eradication

#### Malware Removal
```bash
# Identify malware
# - Hash files and check VirusTotal
# - Behavioral analysis
# - Memory forensics

# Remove persistence
# - Registry keys
# - Scheduled tasks
# - Services
# - Startup items
# - Cron jobs

# Patch vulnerabilities
# Reset compromised credentials
# Rebuild if necessary
```

### Phase 5: Recovery

```bash
# Restore from clean backup
# Verify system integrity
# Monitor for re-infection
# Gradual service restoration
# Enhanced logging
```

### Phase 6: Lessons Learned

```markdown
# Post-Incident Report Template

## Incident Summary
- Date/Time detected:
- Date/Time contained:
- Date/Time resolved:
- Incident type:
- Systems affected:

## Timeline of Events
[Chronological list of events]

## Root Cause Analysis
[How did the incident occur?]

## Impact Assessment
- Data affected:
- Systems compromised:
- Business impact:
- Regulatory implications:

## Response Effectiveness
- What worked well?
- What could be improved?

## Recommendations
1. [Immediate fixes]
2. [Short-term improvements]
3. [Long-term strategic changes]

## Action Items
| Item | Owner | Due Date | Status |
|------|-------|----------|--------|
```

## Memory Forensics

### Volatility 3
```bash
# List processes
vol3 -f memory.dmp windows.pslist
vol3 -f memory.dmp windows.pstree

# Network connections
vol3 -f memory.dmp windows.netscan
vol3 -f memory.dmp windows.netstat

# Command history
vol3 -f memory.dmp windows.cmdline
vol3 -f memory.dmp windows.consoles

# Detect injected code
vol3 -f memory.dmp windows.malfind

# Registry
vol3 -f memory.dmp windows.registry.hivelist
vol3 -f memory.dmp windows.registry.printkey

# Dump suspicious process
vol3 -f memory.dmp windows.memmap --pid 1234 --dump
```

### Acquiring Memory
```bash
# Windows
winpmem_mini_x64.exe memory.raw

# Linux
sudo dd if=/dev/mem of=memory.raw
# Or use LiME kernel module
```

## Disk Forensics

### Evidence Acquisition
```bash
# Create forensic image
dd if=/dev/sda of=disk.img bs=4M status=progress
dc3dd if=/dev/sda of=disk.img hash=sha256 log=acquisition.log

# Mount read-only
mount -o ro,noexec,nodev disk.img /mnt/evidence
```

### Autopsy/Sleuth Kit
```bash
# File system timeline
fls -r -m "/" disk.img > bodyfile.txt
mactime -b bodyfile.txt > timeline.csv

# Deleted file recovery
fls -d disk.img
icat disk.img [inode] > recovered_file
```

## Log Analysis

### Windows Event IDs to Monitor
| Event ID | Description |
|----------|-------------|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4648 | Explicit credential logon |
| 4672 | Admin logon |
| 4688 | Process creation |
| 4697 | Service installed |
| 4698 | Scheduled task created |
| 4720 | User account created |
| 4732 | User added to local group |
| 7045 | Service installed |

### Linux Logs
```bash
# Authentication
/var/log/auth.log
/var/log/secure

# System
/var/log/syslog
/var/log/messages
journalctl

# Web server
/var/log/apache2/access.log
/var/log/nginx/access.log
```

## IOC Collection

### File-based IOCs
```bash
# Hash files
sha256sum suspicious_file
md5sum suspicious_file

# Check on VirusTotal
# API: vt file <hash>
```

### Network IOCs
```bash
# Suspicious IPs
# Suspicious domains
# User-agent strings
# URLs
# Certificates
```

### Host-based IOCs
```bash
# Registry keys
# File paths
# Service names
# Scheduled task names
# Mutex names
```

## Communication Templates

### Initial Notification
```
SECURITY INCIDENT - [SEVERITY]

Time Detected: [TIME]
Systems Affected: [SYSTEMS]
Current Status: [INVESTIGATING/CONTAINED/RESOLVED]

Brief Description:
[What happened]

Immediate Actions Taken:
[Actions]

Next Steps:
[Plan]

Contact: [IR Lead] at [Contact Info]
```

### Status Update
```
INCIDENT UPDATE - [INCIDENT ID]

Status: [CURRENT STATUS]
Time: [UPDATE TIME]

Progress Since Last Update:
- [Action 1]
- [Action 2]

Current Focus:
[What we're working on]

ETA for Next Update: [TIME]
```

## Tools Summary

| Category | Tools |
|----------|-------|
| Memory | Volatility, Rekall |
| Disk | Autopsy, FTK, Sleuth Kit |
| Network | Wireshark, NetworkMiner, Zeek |
| Logs | Splunk, ELK, Graylog |
| Malware | Any.Run, VirusTotal, Cuckoo |
| Timeline | log2timeline/plaso |

## References
- NIST SP 800-61: https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final
- SANS IR Handbook: https://www.sans.org/white-papers/
- MITRE ATT&CK: https://attack.mitre.org
