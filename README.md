# 🔐 LifeOps Auth Service

Identity, authentication, authorization, and subscription management service for the LifeOps platform.

---

## 🧠 Overview

The Auth Service is the **central identity backbone** of LifeOps. Every request across all microservices is authenticated and traced back to a token issued here.

### Core Responsibilities

* User registration & login
* JWT access & refresh token lifecycle
* Session management (multi-device support)
* Subscription lifecycle (Free, Basic, Pro, Max)
* Role-based access control (USER, ADMIN, SUPER_ADMIN)
* Feature-access gating based on subscription plan
* Security enforcement (rate limiting, CSRF, token rotation)
* Audit logging for all sensitive actions

---

## 🏗️ Architecture

* **Framework:** FastAPI (async)
* **Database:** MongoDB (Beanie ODM)
* **Cache & Events:** Redis
* **Auth:** JWT (RS256) + Refresh Tokens
* **API Layer:** GraphQL (Strawberry Federation)
* **Internal Communication:** REST (for token validation)
* **Deployment:** Docker + Nginx

---

## 📁 Project Structure

```
app/
├── config/         # Environment, DB, Redis configs
├── core/           # Security, dependencies, shared logic
├── models/         # MongoDB models (Beanie)
├── schemas/        # Internal Pydantic schemas
├── graphql/        # GraphQL schema & resolvers
├── services/       # Business logic
├── repositories/   # DB access abstraction
├── events/         # Redis pub/sub
├── middleware/     # FastAPI middleware
├── api/internal/   # Internal REST endpoints
├── workers/        # Background jobs
└── constants/      # Enums, limits, configs
```

---

## 🔐 Authentication Model

### Token Strategy

| Token              | Storage           | Expiry  |
| ------------------ | ----------------- | ------- |
| Access Token (JWT) | Memory (frontend) | 15 min  |
| Refresh Token      | HttpOnly Cookie   | 30 days |

### Flow

1. User logs in → receives access + refresh token
2. Access token used for API calls
3. When expired → refresh token generates new access token
4. Refresh token is rotated on every use

---

## 📡 Internal Endpoints

These are used by other services (NOT public):

```
GET /internal/validate-token
GET /internal/check-access
```

### Example

```bash
curl http://auth-service:8001/internal/validate-token \
  -H "Authorization: Bearer <token>"
```

---

## 🔄 GraphQL API

### Entry Point

```
http://localhost:8001/graphql
```

### Key Mutations

* `register`
* `login`
* `refreshToken`
* `logout`
* `startTrial`
* `subscribeToPlan`

### Key Queries

* `me`
* `activeSubscription`
* `activeSessions`
* `planPricing`

---

## 💳 Subscription System

### Plans

* FREE
* BASIC
* PRO
* MAX

### Features

* Plan-based feature gating
* Grace period (3 days)
* Trial support (7 days Pro)
* Upgrade/downgrade handling
* Auto-renewal support

---

## 🔒 Security Features

* bcrypt password hashing (cost factor 12)
* RS256 JWT signing (asymmetric keys)
* CSRF protection (double-submit cookie)
* Rate limiting (slowapi)
* Refresh token rotation
* Brute-force login protection
* Secure cookies (HttpOnly, SameSite)

---

## 🚀 Getting Started

### 1. Clone repo

```bash
git clone <repo-url>
cd lifeops-auth-service
```

---

### 2. Create environment file

```bash
cp .env.example .env
```

---

### 3. Start dependencies

```bash
docker-compose up -d
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run service

```bash
uvicorn app.main:app --reload --port 8001
```

---

### 6. Open GraphQL Playground

```
http://localhost:8001/graphql
```

---

## 🧪 Testing

```bash
pytest tests/ -v
```

Uses:

* `mongomock-motor` (in-memory MongoDB)
* `fakeredis` (in-memory Redis)

---

## 📊 Events (Redis)

### Published

* `user_registered`
* `user_logged_in`
* `subscription_started`
* `subscription_expired`

### Consumed

* Payment confirmation events
* Notification triggers

---

## 🛠️ Scripts

```bash
python scripts/create_admin.py
python scripts/seed_plans.py
python scripts/generate_keys.py
```

---

## 🧱 Deployment

* Dockerized service
* Nginx reverse proxy
* CI/CD via GitHub Actions

---

## ⚠️ Important Design Rules

* ❌ No business logic in GraphQL resolvers
* ❌ No password storage outside Auth Service
* ❌ No direct DB access outside repositories
* ✅ Always use services layer
* ✅ Always log sensitive actions

---

## 🧑‍💻 Author

LifeOps — Solo Developer System
Built for scalability, clarity, and long-term independence.

---
