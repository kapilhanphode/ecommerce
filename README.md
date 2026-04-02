# ecommerce

# 🛒 Multi-Vendor eCommerce Backend (Django DRF)

A **production-grade multi-vendor eCommerce backend** built using Django REST Framework with clean architecture, scalable design, and real-world payment & wallet systems.

🚀 **Live Deployment:** Hosted on Railway using Docker
📦 **Architecture:** Service + Selector Pattern (Clean Architecture)

---

## ⚙️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** PostgreSQL
* **Cache & Queue:** Redis
* **Async Tasks:** Celery
* **Authentication:** JWT
* **Deployment:** Docker + Railway
* **Web Server:** Gunicorn
* **Reverse Proxy:** Nginx (production-ready setup)

---

## 🧩 Core Features

### 🛍️ Product Management

* Vendor-based product creation
* Category & variant support
* Search, filter, ordering

### 🛒 Cart & Orders

* Cart system with variant support
* Atomic order creation
* Inventory validation & stock deduction

### 💳 Payments System

* Idempotent payment processing
* Vendor-wise payment splitting
* Platform commission handling
* Race condition safe (`select_for_update`)

### 👛 Wallet System

* Vendor wallet credit on successful payment
* Wallet debit on refund
* Full transaction history tracking

### 🔁 Refund & Returns

* Return request workflow (User → Admin approval)
* Refund triggered only after approval
* Vendor-level refund handling
* Wallet safety (no negative balance)

### 💸 Payout System

* Vendors can request payouts
* Balance validation before payout
* Transaction logging

---

## 🔐 Security & Reliability

* JWT Authentication
* Role-based permissions (Admin / Vendor / Customer)
* API Throttling
* Idempotency for payment safety
* Database transactions & row-level locking
* Centralized exception handling

---

## ⚡ Performance Optimizations

* PostgreSQL (production DB)
* Redis caching
* Query optimization (`select_related`, indexing)
* Background jobs using Celery
* Optimized API responses & pagination

---

## 📨 Notifications

* Email notifications (async via Celery)
* Payment success emails
* Refund processed emails

---

## 🧪 Testing

* Unit tests for:

  * Order flow
  * Payment flow
  * Refund flow

---

## 📁 Project Structure

```
apps/
  products/
  cart/
  orders/
  payments/
  wallet/
  returns/
  inventory/
  notifications/
  accounts/
  core/

config/
  settings/
    base.py
    dev.py
    prod.py
```

---

## 🐳 Docker Deployment

The project is fully containerized using Docker.

### Services:

* Django App (Gunicorn)
* PostgreSQL
* Redis
* Celery Worker
* Celery Beat

### Run Locally:

```bash
docker-compose build
docker-compose up
```

---

## ☁️ Deployment (Railway)

* Containerized using Docker
* Deployed on Railway
* PostgreSQL + Redis configured
* Environment variables managed securely

---

## 🔑 Environment Variables

```
DEBUG=0
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://...
REDIS_URL=redis://...
DJANGO_ALLOWED_HOSTS=*
```

---

## 🚀 API Highlights

* `/api/auth/` → Authentication
* `/api/products/` → Product APIs
* `/api/cart/` → Cart APIs
* `/api/orders/` → Order APIs
* `/api/payments/` → Payment processing
* `/api/wallet/` → Wallet management
* `/api/returns/` → Return & refund system

---

## 📌 Key Highlights

✔ Production-ready architecture
✔ Multi-vendor support
✔ Payment split logic
✔ Wallet + payout system
✔ Idempotent APIs
✔ Fully Dockerized
✔ Deployed on Railway

---

## 👨‍💻 Author

Built with focus on **real-world backend engineering practices** and production readiness.

---

## ⭐ Future Improvements

* Payment gateway integration (Stripe/Razorpay)
* Advanced analytics dashboard
* Webhooks support
* Microservices architecture

---
