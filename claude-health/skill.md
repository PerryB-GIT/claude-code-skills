# Claude Health Check

Quick diagnostic of Claude Code system health. Use when experiencing slowness, high memory usage, or MCP issues.

## Invocation
- `/claude-health` or `/health`

## What This Skill Does

Run a comprehensive health check that reports:

1. **Node Processes**: Count and total memory usage
2. **MCP Status**: Connected, failed, or needs authentication
3. **System Memory**: Total, used, available with percentage
4. **Versions**: Claude Code and Node.js versions
5. **Overall Status**: HEALTHY, NEEDS ATTENTION, or CRITICAL

## Instructions

When this skill is invoked, run the following diagnostic commands in parallel:

### Step 1: Gather Data (parallel)
```bash
# Node processes
tasklist | grep -i node

# MCP status
claude mcp list

# System memory
systeminfo | grep -i "Memory"

# Versions
claude --version && node --version
```

### Step 2: Analyze and Report

Present findings in this format:

```
## Claude Code Health Report

### Processes
| Type | Count | Memory |
|------|-------|--------|
| Node.js | X | XXX MB |
| Python | X | XX MB |

### MCP Servers
| Server | Status |
|--------|--------|
| gmail | ✓ Connected |
| ... | ... |

### System Memory
- Total: XX GB
- Used: XX GB (XX%)
- Available: XX GB

### Overall Status: [STATUS]
[Any recommendations if issues found]
```

### Status Thresholds
- **HEALTHY**: <15 node processes, <70% memory, all MCPs connected
- **NEEDS ATTENTION**: 15-25 node processes OR 70-85% memory OR failed MCPs
- **CRITICAL**: >25 node processes OR >85% memory

### Recommendations to Include
- If high process count: "Consider closing unused Claude instances"
- If high memory: "Close unused applications or Claude instances"
- If MCPs failed: "Run `claude mcp list` to diagnose, may need restart"
- If MCPs need auth: "Re-authenticate with `cd ~/mcp-servers/[name] && npm run auth`"
