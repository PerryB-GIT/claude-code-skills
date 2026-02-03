# Google Voice Receptionist Check

Quick status check on the GV Receptionist system. Use to verify monitoring is running, check for new messages, and view scheduled task status.

## Invocation
- `/gv-check` or `/gv`

## What This Skill Does

1. **Process Status**: Is the GV Receptionist running?
2. **Scheduled Tasks**: Status of GVMessageChecker, GVDailySummary, GVReceptionist
3. **Recent Messages**: Check for new voicemails/SMS in last 24 hours
4. **Logs**: Show recent log entries

## Reference Information

### File Locations
- Main Script: `~/mcp-servers/gv-receptionist/gv-receptionist.js`
- Message Checker: `~/mcp-servers/gv-receptionist/check-gv-messages.js`
- Log File: `~/mcp-servers/gv-receptionist/gv-receptionist.log`
- Check Log: `~/mcp-servers/gv-receptionist/gv-check.log`
- Processed Messages: `~/mcp-servers/gv-receptionist/processed-messages.json`

### Phone Numbers
- Business Line: {BUSINESS_PHONE}
- Personal (for commands): {PERSONAL_PHONE}

### Scheduled Tasks
| Task | Schedule | Purpose |
|------|----------|---------|
| GVMessageChecker | Every 5 minutes | Checks Gmail for new voicemails |
| GVDailySummary | 8:00 AM daily | Shows summary notification |
| GVReceptionist | At logon | Background monitoring |

## Instructions

When this skill is invoked, run these checks:

### Step 1: Check Process Status
```bash
tasklist | grep -i node | grep -i gv
```

Also check if any gv-receptionist processes are running:
```bash
wmic process where "name='node.exe'" get ProcessId,CommandLine 2>&1 | grep -i gv-receptionist
```

### Step 2: Check Scheduled Tasks
```powershell
Get-ScheduledTask -TaskName 'GV*' | Select-Object TaskName, State | Format-Table
```

### Step 3: Check Recent Logs
```bash
tail -20 ~/mcp-servers/gv-receptionist/gv-receptionist.log 2>/dev/null || echo "No main log found"
tail -10 ~/mcp-servers/gv-receptionist/gv-check.log 2>/dev/null || echo "No check log found"
```

### Step 4: Check Processed Messages Count
```bash
cat ~/mcp-servers/gv-receptionist/processed-messages.json 2>/dev/null | grep -c '"' || echo "0"
```

### Step 5: Present Report

```
## GV Receptionist Status

### Process Status
- Main Receptionist: [RUNNING / NOT RUNNING]
- PID: [if running]

### Scheduled Tasks
| Task | Status |
|------|--------|
| GVMessageChecker | [Ready/Running/Disabled] |
| GVDailySummary | [Ready/Running/Disabled] |
| GVReceptionist | [Ready/Running/Disabled] |

### Message Stats
- Processed messages: XX
- Last check: [timestamp from log]

### Recent Log Entries
[Last 5 relevant log entries]

### Quick Actions
- Start receptionist: `node ~/mcp-servers/gv-receptionist/gv-receptionist.js`
- Run message check: `Start-ScheduledTask -TaskName 'GVMessageChecker'`
- View full log: `Get-Content ~/mcp-servers/gv-receptionist/gv-receptionist.log -Tail 50`
```

### Troubleshooting Suggestions

If receptionist not running:
- "Start with: `node ~/mcp-servers/gv-receptionist/gv-receptionist.js`"
- "Or enable scheduled task: `Enable-ScheduledTask -TaskName 'GVReceptionist'`"

If scheduled tasks disabled:
- "Enable with: `Enable-ScheduledTask -TaskName 'GVMessageChecker'`"

If Gmail auth issues in logs:
- "Re-authenticate: `cd ~/mcp-servers/gmail && npm run auth`"
