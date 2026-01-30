# NEMATI AI SDK - Complete Roadmap

---

## Overview Timeline

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           NEMATI AI SDK ROADMAP                                  │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  PHASE 1        PHASE 2        PHASE 3        PHASE 4        PHASE 5           │
│  Foundation     Core APIs      Extended       Polish &       Growth            │
│  (Week 1-2)     (Week 3-4)     (Week 5-6)     Launch (W7-8)  (Ongoing)         │
│                                                                                  │
│  ████████░░     ░░░░░░░░░░     ░░░░░░░░░░     ░░░░░░░░░░     ░░░░░░░░░░        │
│                                                                                  │
│  • API Key      • Chat API     • Audio API    • Docs         • JS SDK          │
│  • Auth         • Writer API   • Trends API   • Examples     • Analytics       │
│  • Account      • Image API    • Market API   • PyPI         • Webhooks        │
│    Endpoints    • Docs API     • Rate Limits  • Launch       • Enterprise      │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Foundation (Week 1-2)

### Goal: API Key system + Account endpoints + SDK base

### 1.1 Backend - API Key Management

| Task | Description | Time |
|------|-------------|------|
| Create `apps/sdk/` app | New Django app for SDK | 1 hour |
| APIKey model | Store keys with hash, scopes, limits | 2 hours |
| API Key authentication | X-API-Key header auth | 2 hours |
| Key generation service | Generate `nai_live_xxx` keys | 1 hour |
| Key endpoints | Create, List, Revoke keys | 2 hours |
| Rate limiting middleware | Per-key rate limits | 2 hours |

**Files to create:**
```
apps/sdk/
├── __init__.py
├── apps.py
├── models/
│   ├── __init__.py
│   └── api_key.py
├── api/
│   ├── __init__.py
│   ├── router.py
│   ├── auth.py
│   └── views/
│       └── api_key_views.py
├── services/
│   └── api_key_service.py
└── middleware.py
```

### 1.2 Backend - Account Endpoints

**Backend Implementation:** `apps/subscription/api/sdk_views.py`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/sdk/account/me/` | GET | Get account info |
| `/sdk/account/credits/` | GET | Get credit balance |
| `/sdk/account/usage/` | GET | Get usage stats |
| `/sdk/account/limits/` | GET | Get plan limits |
| `/sdk/account/api-keys/` | GET | List API keys |
| `/sdk/account/api-keys/` | POST | Create API key |
| `/sdk/account/api-keys/{id}/` | DELETE | Revoke API key |

### 1.3 Frontend - API Keys Dashboard

| Task | Description | Time |
|------|-------------|------|
| API Keys page | `/dashboard/api-keys/` | 4 hours |
| Create key modal | Generate + show key once | 2 hours |
| Key list component | Show masked keys | 2 hours |
| Revoke confirmation | Delete key flow | 1 hour |
| Copy to clipboard | One-click copy | 30 min |

**UI Mockup:**
```
┌─────────────────────────────────────────────────────────────────┐
│  🔑 API Keys                                    [+ Create Key]  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Your API keys are used to authenticate SDK requests.           │
│  Keep them secret - never share in public code.                 │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ 🟢 Production                                               │ │
│  │    nai_live_****************************abcd               │ │
│  │    Created: Jan 28, 2026 • Last used: 2 hours ago          │ │
│  │    Scopes: All                                              │ │
│  │                                        [📋 Copy] [🗑 Revoke] │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │ 🟢 Development                                              │ │
│  │    nai_test_****************************efgh               │ │
│  │    Created: Jan 20, 2026 • Last used: 5 days ago           │ │
│  │    Scopes: chat, writer                                     │ │
│  │                                        [📋 Copy] [🗑 Revoke] │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ─────────────────────────────────────────────────────────────  │
│                                                                  │
│  📊 Usage This Month                                            │
│  ├── API Requests: 12,450 / 50,000                             │
│  ├── Credits Used: 2,340 / 10,000                              │
│  └── Rate Limit: 60 req/min                                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 1.4 Phase 1 Deliverables

- [ ] API Key model with secure hashing
- [ ] API Key CRUD endpoints
- [ ] X-API-Key authentication
- [ ] Account info endpoints
- [ ] Frontend API Keys page
- [ ] Key creation modal (show once)
- [ ] Python SDK connects successfully

---

## Phase 2: Core APIs (Week 3-4)

### Goal: Chat, Writer, Image, Documents endpoints

### 2.1 Backend - SDK Router Structure

```python
# core/api.py
api.add_router("/sdk/", sdk_router)

# SDK Router structure:
/api/v1/sdk/
├── account/          # ✅ Phase 1
├── chat/             # Phase 2
├── writer/           # Phase 2
├── image/            # Phase 2
└── documents/        # Phase 2
```

### 2.2 Chat API

**Backend Implementation:** `apps/chat/api/sdk_views.py`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/sdk/chat/completions/` | POST | Create chat completion |
| `/sdk/chat/completions/` | POST (stream) | Streaming chat |
| `/sdk/chat/conversations/` | GET | List conversations |
| `/sdk/chat/conversations/` | POST | Create conversation |
| `/sdk/chat/conversations/{id}/` | GET | Get conversation |
| `/sdk/chat/conversations/{id}/` | DELETE | Delete conversation |

**Request/Response:**
```python
# Request
{
    "messages": [
        {"role": "system", "content": "You are helpful."},
        {"role": "user", "content": "Hello!"}
    ],
    "model": "gpt-4",
    "max_tokens": 1000,
    "temperature": 0.7,
    "stream": false
}

# Response
{
    "success": true,
    "data": {
        "id": "chat_abc123",
        "content": "Hello! How can I help you?",
        "role": "assistant",
        "model": "gpt-4",
        "finish_reason": "stop",
        "usage": {
            "prompt_tokens": 20,
            "completion_tokens": 10,
            "total_tokens": 30,
            "credits": 1.5
        }
    },
    "meta": {
        "request_id": "req_xyz789",
        "latency_ms": 450
    }
}
```

### 2.3 Writer API

**Backend Implementation:** `apps/AI_writer/api/sdk_views.py`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/sdk/writer/generate/` | POST | Generate content |
| `/sdk/writer/rewrite/` | POST | Rewrite content |
| `/sdk/writer/summarize/` | POST | Summarize content |
| `/sdk/writer/templates/` | GET | List templates |
| `/sdk/writer/templates/{id}/` | GET | Get template |
| `/sdk/writer/templates/{id}/generate/` | POST | Generate from template |

### 2.4 Image API

**Backend Implementation:** `apps/image/api/sdk_views.py`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/sdk/image/generate/` | POST | Text to image |
| `/sdk/image/edit/` | POST | Image to image |
| `/sdk/image/upscale/` | POST | Upscale image |
| `/sdk/image/variations/` | POST | Create variations |

### 2.5 Documents API

**Backend Implementation:** `apps/chat_pdf/api/sdk_views.py`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/sdk/documents/` | GET | List documents |
| `/sdk/documents/upload/` | POST | Upload document |
| `/sdk/documents/{id}/` | GET | Get document |
| `/sdk/documents/{id}/` | DELETE | Delete document |
| `/sdk/documents/chat/` | POST | Chat with document |
| `/sdk/documents/convert/` | POST | Convert document |

### 2.6 Phase 2 Deliverables

- [ ] Chat completions endpoint (sync)
- [ ] Chat streaming endpoint (SSE)
- [ ] Writer generate endpoint
- [ ] Writer templates endpoints
- [ ] Image generate endpoint
- [ ] Image edit/upscale endpoints
- [ ] Documents upload/chat endpoints
- [ ] Credit deduction integration
- [ ] Usage logging per API key

---

## Phase 3: Extended APIs (Week 5-6)

### Goal: Audio, Trends, Market + Rate Limiting

### 3.1 Audio API

**Backend Implementation:** `apps/audio/api/sdk_views.py`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/sdk/audio/speech/` | POST | Text to speech |
| `/sdk/audio/transcribe/` | POST | Speech to text |
| `/sdk/audio/translate/` | POST | Translate audio |

### 3.2 Trends API

**Backend Implementation:** `apps/trend_discovery/api/sdk_views.py`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/sdk/trends/search/` | POST | Multi-platform search |
| `/sdk/trends/analyze/` | POST | Analyze trend |
| `/sdk/trends/platforms/` | GET | List platforms |
| `/sdk/trends/youtube/trending/` | GET | YouTube trending |
| `/sdk/trends/tiktok/trending/` | GET | TikTok trending |
| `/sdk/trends/reddit/trending/` | GET | Reddit trending |

### 3.3 Market API

**Backend Implementation:** `apps/market_intel/api/sdk_views.py`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/sdk/market/search/` | GET | Search symbols |
| `/sdk/market/analyze/` | POST | AI market analysis |
| `/sdk/market/stocks/{symbol}/` | GET | Stock data |
| `/sdk/market/stocks/{symbol}/history/` | GET | Stock history |
| `/sdk/market/crypto/{symbol}/` | GET | Crypto data |
| `/sdk/market/crypto/{symbol}/history/` | GET | Crypto history |
| `/sdk/market/crypto/` | GET | List top cryptos |

### 3.4 Rate Limiting System

```python
# Rate limit tiers by plan
RATE_LIMITS = {
    "Pro": {
        "per_minute": 60,
        "per_hour": 1000,
        "per_day": 10000,
    },
    "Business": {
        "per_minute": 300,
        "per_hour": 5000,
        "per_day": 100000,
    },
}
```

**Response headers:**
```
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 45
X-RateLimit-Reset: 1706500000
```

### 3.5 Phase 3 Deliverables

- [ ] Audio TTS endpoint
- [ ] Audio STT endpoint
- [ ] Trends search endpoint
- [ ] Trends platform endpoints
- [ ] Market stocks endpoints
- [ ] Market crypto endpoints
- [ ] Rate limiting middleware
- [ ] Rate limit headers
- [ ] 429 response handling

---

## Phase 4: Polish & Launch (Week 7-8)

### Goal: Documentation, Examples, PyPI publish

### 4.1 API Documentation

**Create OpenAPI spec:**
```yaml
# openapi.yaml
openapi: 3.0.3
info:
  title: Nemati AI API
  version: 1.0.0
  description: Official API for Nemati AI services
servers:
  - url: https://api.nemati.ai/v1/sdk
paths:
  /chat/completions:
    post:
      summary: Create chat completion
      security:
        - ApiKeyAuth: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ChatRequest'
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatResponse'
```

### 4.2 Documentation Site

```
docs.nemati.ai/
├── Getting Started
│   ├── Introduction
│   ├── Authentication
│   ├── Quick Start
│   └── Rate Limits
├── API Reference
│   ├── Chat
│   ├── Writer
│   ├── Image
│   ├── Audio
│   ├── Trends
│   ├── Market
│   ├── Documents
│   └── Account
├── SDKs
│   ├── Python
│   ├── JavaScript (coming soon)
│   └── REST API
├── Guides
│   ├── Building a Chatbot
│   ├── Content Generation
│   ├── Trend Analysis
│   └── Market Dashboard
└── Support
    ├── FAQ
    ├── Error Codes
    └── Contact
```

### 4.3 Python SDK Publish

```bash
# 1. Build package
pip install build twine
python -m build

# 2. Test on TestPyPI first
twine upload --repository testpypi dist/*

# 3. Test installation
pip install --index-url https://test.pypi.org/simple/ nemati-ai

# 4. Publish to PyPI
twine upload dist/*
```

### 4.4 Launch Checklist

- [ ] All endpoints tested
- [ ] OpenAPI spec complete
- [ ] Documentation site live
- [ ] Python SDK on PyPI
- [ ] Examples repository
- [ ] Error codes documented
- [ ] Rate limits documented
- [ ] Pricing page updated (API access)
- [ ] Blog post: "Introducing Nemati AI API"
- [ ] Email to existing Pro/Business users

### 4.5 Phase 4 Deliverables

- [ ] OpenAPI specification
- [ ] Documentation site
- [ ] Python SDK v1.0.0 on PyPI
- [ ] Examples repository
- [ ] API status page
- [ ] Launch announcement

---

## Phase 5: Growth (Ongoing)

### 5.1 JavaScript/TypeScript SDK

```
nemati-js/
├── package.json
├── src/
│   ├── index.ts
│   ├── client.ts
│   ├── resources/
│   └── models/
└── dist/
```

**Usage:**
```javascript
import { NematiAI } from 'nemati-ai';

const client = new NematiAI({ apiKey: 'nai_live_xxx' });

const response = await client.chat.create({
  messages: [{ role: 'user', content: 'Hello!' }]
});
```

### 5.2 Webhooks System

```python
# User can register webhooks for events
POST /sdk/webhooks/
{
    "url": "https://example.com/webhook",
    "events": ["chat.completed", "image.generated", "credits.low"]
}
```

### 5.3 Analytics Dashboard

```
┌─────────────────────────────────────────────────────────────────┐
│  📊 API Analytics                              Last 30 days ▼   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Total Requests        Success Rate         Avg Latency         │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐    │
│  │   245,892    │     │    99.2%     │     │    342ms     │    │
│  │   ↑ 12.5%    │     │    ↑ 0.3%    │     │    ↓ 8.2%    │    │
│  └──────────────┘     └──────────────┘     └──────────────┘    │
│                                                                  │
│  [========================================] Requests over time   │
│                                                                  │
│  Top Endpoints:                                                  │
│  1. /chat/completions     - 156,234 requests (63.5%)           │
│  2. /image/generate       - 45,123 requests (18.4%)            │
│  3. /writer/generate      - 28,456 requests (11.6%)            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 5.4 Enterprise Features

| Feature | Description |
|---------|-------------|
| Custom rate limits | Negotiated limits |
| Dedicated support | Priority support channel |
| SLA guarantee | 99.9% uptime |
| Custom models | Fine-tuned models |
| On-premise option | Self-hosted deployment |
| SSO/SAML | Enterprise authentication |
| Audit logs | Compliance logging |

### 5.5 Phase 5 Deliverables

- [ ] JavaScript SDK on npm
- [ ] Webhooks system
- [ ] Analytics dashboard
- [ ] Enterprise tier
- [ ] Partner program
- [ ] API marketplace listing

---

## Summary - Priority Tasks

### Immediate (This Week)

| # | Task | Time | Priority |
|---|------|------|----------|
| 1 | Create `apps/sdk/` Django app | 1h | 🔴 High |
| 2 | APIKey model | 2h | 🔴 High |
| 3 | API Key authentication | 2h | 🔴 High |
| 4 | Account endpoints | 3h | 🔴 High |
| 5 | Frontend API Keys page | 4h | 🔴 High |

### Next 2 Weeks

| # | Task | Time | Priority |
|---|------|------|----------|
| 6 | Chat API endpoint | 4h | 🔴 High |
| 7 | Chat streaming | 3h | 🔴 High |
| 8 | Writer API endpoint | 3h | 🟡 Medium |
| 9 | Image API endpoint | 3h | 🟡 Medium |
| 10 | Rate limiting | 3h | 🟡 Medium |

### Before Launch

| # | Task | Time | Priority |
|---|------|------|----------|
| 11 | OpenAPI spec | 4h | 🟡 Medium |
| 12 | Documentation | 8h | 🟡 Medium |
| 13 | PyPI publish | 2h | 🟡 Medium |
| 14 | Examples | 4h | 🟢 Low |
| 15 | Blog post | 2h | 🟢 Low |

---

## File Structure - Final

```
Backend:
apps/sdk/
├── __init__.py
├── apps.py
├── models/
│   ├── __init__.py
│   ├── api_key.py
│   └── webhook.py
├── api/
│   ├── __init__.py
│   ├── router.py
│   ├── auth.py
│   ├── schemas/
│   │   ├── common.py
│   │   ├── chat.py
│   │   ├── writer.py
│   │   ├── image.py
│   │   ├── audio.py
│   │   ├── trends.py
│   │   ├── market.py
│   │   ├── documents.py
│   │   └── account.py
│   └── views/
│       ├── api_key_views.py
│       ├── chat_views.py
│       ├── writer_views.py
│       ├── image_views.py
│       ├── audio_views.py
│       ├── trends_views.py
│       ├── market_views.py
│       ├── documents_views.py
│       └── account_views.py
├── services/
│   ├── api_key_service.py
│   └── usage_service.py
├── middleware.py
└── throttling.py

Frontend:
src/pages/dashboard/
└── api-keys/
    ├── index.tsx
    ├── CreateKeyModal.tsx
    └── KeyList.tsx

SDKs:
github.com/nemati-ai/nemati-ai   ✅ Done
github.com/nemati-ai/nemati-js       Phase 5
```

---

**Ready to start Phase 1?** I can give you the full code for the API Key system.