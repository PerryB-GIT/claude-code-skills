# Claude Code Skills & Agents

Personal skill library for Claude Code, built by {YOUR_NAME}.

## 📁 Skill Categories

### 🎙️ Executive Assistant (Evie)
**Your AI-powered British executive assistant with voice, vision, and proactive intelligence.**

| Skill | Description |
|-------|-------------|
| `executive-assistant/` | Main Evie skill with voice interaction, calendar, email, and proactive life management |
| `executive-assistant/voice/evie-speak-edge.py` | Natural British TTS with Edge (free, no API key) |
| `executive-assistant/voice/evie-listen.py` | Speech-to-text with Whisper |
| `executive-assistant/voice/evie-vision.py` | Camera and screen capture |
| `executive-assistant/voice/evie-interactive.py` | Full interactive mode with intents |

---

### 💼 Sales & Business Development

| Skill | Description |
|-------|-------------|
| `sales-agent/` | Master sales toolkit - prospecting to closing |
| `sales-discovery/` | SPIN selling, MEDDIC/BANT qualification |
| `sales-demo/` | Demo structure, objection handling |
| `sales-closing/` | Negotiation tactics, closing techniques |
| `sales-ops/` | Pipeline management, forecasting, CRM |
| `founder-led-sales/` | Early-stage startup sales (0-$500K ARR) |
| `cold-email-outreach/` | Cold email sequences, templates |
| `negotiator/` | BATNA analysis, contract negotiation |

---

### 📊 Project & Product Management

| Skill | Description |
|-------|-------------|
| `pm-agent/` | Master PM toolkit - project + product |
| `project-management-pmp/` | PMBOK processes, WBS, Gantt, earned value |
| `product-management/` | PRDs, roadmaps, prioritization |
| `product-manager-toolkits/` | RICE, Kano, JTBD frameworks |
| `agile-scrum-master/` | Sprints, velocity, retrospectives |
| `stakeholder-management/` | RACI, communication plans |
| `risk-management/` | Risk registers, mitigation strategies |
| `prd/` | Product Requirements Document generator |
| `ralph/` | PRD to prd.json converter for Ralph |

---

### 🔐 Security & Incident Response

| Skill | Description |
|-------|-------------|
| `ceh-agent/` | Certified Ethical Hacker toolkit - pentesting, OWASP |
| `incident-response/` | Site downtime triage, server diagnostics |
| `incident-response-cyber/` | NIST IR framework, forensics |
| `webapp-security/` | Web application security testing |
| `osint-recon/` | Open source intelligence gathering |
| `threat-intel/` | Threat intelligence analysis |
| `ffuf_claude_skill/` | Web fuzzing with ffuf |

---

### ☁️ AWS & Cloud

| Skill | Description |
|-------|-------------|
| `aws-cost/` | AWS Cost Explorer analysis |
| `aws-cost-optimizer/` | Spending analysis, unused resources, RI recommendations |
| `aws-health-check/` | AWS resource health monitoring |

---

### 💰 Finance & Accounting

| Skill | Description |
|-------|-------------|
| `creating-financial-models/` | SaaS metrics, P&L, cap tables, DCF |
| `managing-finances/` | Business expense tracking, budgeting |
| `invoice-generator/` | Professional invoice creation |
| `creating-invoices/` | Billing templates, payment tracking |
| `investment-agent/` | Investment analysis and research |
| `mortgage-agent/` | Mortgage calculations, comparisons |
| `consulting-accountants/` | Bookkeeper/accountant workflows |
| `consulting-wealth-managers/` | Financial advisor workflows |

---

### 👥 Client Management

| Skill | Description |
|-------|-------------|
| `client-intake/` | New client onboarding, project scoping |
| `client-onboarding/` | Standardized onboarding questionnaire |
| `client-deploy/` | Client site deployment workflows |
| `support-forge-deploy/` | Support Forge specific deployment |

---

### 📧 Email & Marketing

| Skill | Description |
|-------|-------------|
| `email-marketing-agent/` | Campaign strategy, deliverability, compliance |
| `email-automation/` | Email workflow automation |
| `cold-email-outreach/` | Cold outreach sequences |
| `newsletter-creator/` | Newsletter content and design |
| `writing-emails/` | Professional email templates |

---

### 🎨 Content & Creative

| Skill | Description |
|-------|-------------|
| `creating-courses/` | Online course development |
| `creating-graphics/` | Image and logo creation |
| `creating-proposals/` | Business proposals, engagement letters |
| `preparing-meetings/` | Meeting prep, agendas, briefings |
| `researching-prospects/` | Lead research, company intel |

---

### 🔍 SEO & Marketing

| Skill | Description |
|-------|-------------|
| `seo-audit/` | Technical SEO, Core Web Vitals |
| `auditing-seo/` | Website SEO analysis |
| `managing-social-media/` | Social content planning |
| `monitoring-sites/` | Website health monitoring |

---

### 🏠 Real Estate

| Skill | Description |
|-------|-------------|
| `real-estate-agent/` | Property analysis, market research |

---

### 💻 Development

| Skill | Description |
|-------|-------------|
| `back-end-dev-guidelines/` | API design, database patterns, security |
| `senior-backend/` | Architecture decisions, code reviews |
| `skill-builder/` | Create new Claude Code skills |
| `ios-simulator-skill/` | iOS simulator interactions |

---

## 🚀 Quick Start

### Using a Skill
```bash
# Invoke any skill with slash command
/negotiator
/sales-agent
/ceh-agent
/creating-financial-models
```

### Evie Voice Assistant
```bash
# Start interactive mode
python ~/.claude/skills/executive-assistant/voice/evie-interactive.py

# With wake word
python evie-interactive.py --wake-word "hey evie"

# With vision (camera/screen)
python evie-interactive.py --vision
```

### Evie Commands
- "check my calendar" / "what's on my schedule"
- "check my email" / "any new messages"
- "what's the weather" / "weather forecast"
- "any news" / "what's happening today"
- "take a screenshot" / "what am I looking at"
- "help me with [skill]" - invokes any skill
- "goodbye evie" - exits

---

## 📋 Requirements

### Voice Features
```bash
pip install edge-tts SpeechRecognition pyaudio openai-whisper
```

### Vision Features
```bash
pip install opencv-python Pillow mss
```

---

## 🔧 Configuration

Skills are stored in `~/.claude/skills/` and automatically loaded by Claude Code.

Each skill contains:
- `skill.md` - Main skill instructions and templates
- Supporting files (scripts, configs, examples)

---

## 📝 License

Personal use. Built for {YOUR_NAME}' Claude Code workflow.

---

## 🤖 About Evie

Evie is a warm British executive assistant inspired by Evie Hammond. She:
- Uses natural conversational speech with contractions and British expressions
- Tracks your calendar, email, and tasks
- Monitors family birthdays and life events proactively
- Suggests gift ideas, reservations, and thoughtful gestures
- Integrates with all your other skills seamlessly

Voice: en-GB-SoniaNeural (professional) / en-GB-LibbyNeural (casual)
