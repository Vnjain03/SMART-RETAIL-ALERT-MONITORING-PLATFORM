# ⭐ SMART RETAIL ALERT & MONITORING PLATFORM

A production-ready, distributed monitoring and alerting system for retail microservices built with **Python (FastAPI)** and **React**.

![Architecture](https://img.shields.io/badge/Architecture-Microservices-blue)
![Backend](https://img.shields.io/badge/Backend-FastAPI-green)
![Frontend](https://img.shields.io/badge/Frontend-React-61DAFB)
![Database](https://img.shields.io/badge/Database-Azure_Cosmos_DB-0078D4)
![Streaming](https://img.shields.io/badge/Streaming-Apache_Kafka-231F20)
![Orchestration](https://img.shields.io/badge/Orchestration-Kubernetes-326CE5)

## 🎯 Overview

This platform provides real-time monitoring, alerting, and analytics for distributed retail systems. It collects events from multiple microservices, processes them through a sophisticated rules engine, and provides actionable insights through an accessible, real-time dashboard.

### Key Features

- **Real-time Event Streaming**: Apache Kafka-based event pipeline with guaranteed ordering
- **Intelligent Alerting**: Configurable rules engine supporting threshold, rate-based, and statistical anomaly detection
- **Distributed Tracing**: OpenTelemetry + Jaeger for complete request path visualization
- **Auto-scaling**: Kubernetes HPA based on custom metrics (Kafka lag, CPU)
- **Accessibility First**: WCAG 2.2 AA compliant frontend with full keyboard navigation
- **Production-Ready**: Comprehensive monitoring, structured logging, health checks

## 📐 Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         FRONTEND (React)                        │
│                    Material-UI + WebSockets                     │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                     API GATEWAY (FastAPI)                       │
│                  JWT Auth + Request Routing                     │
└───┬─────────────┬─────────────┬─────────────┬──────────────────┘
    │             │             │             │
    ▼             ▼             ▼             ▼
┌─────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐
│ Event   │ │  Alert   │ │  Query   │ │     User     │
│Ingestion│ │  Rules   │ │Analytics │ │  Management  │
│ Service │ │  Engine  │ │ Service  │ │   Service    │
└────┬────┘ └────┬─────┘ └────┬─────┘ └──────┬───────┘
     │           │             │               │
     │           │             │               │
     ▼           ▼             ▼               ▼
┌─────────────────────────────────────────────────────────────────┐
│                    APACHE KAFKA CLUSTER                         │
│     Topics: service-events, alert-events, aggregated-metrics    │
└─────────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    AZURE COSMOS DB (NoSQL)                      │
│      Collections: events, alerts, rules, users, metrics         │
└─────────────────────────────────────────────────────────────────┘
```

## 🛠️ Technology Stack

### Backend Services (All Python + FastAPI)
- **API Gateway**: Request routing, JWT authentication, input validation
- **Event Ingestion**: High-throughput event collection and Kafka publishing
- **Alert Rules Engine**: Real-time rule evaluation and alert generation
- **Query & Analytics**: Historical data access and metric computation
- **User Management**: Authentication, authorization, user profiles

### Frontend
- **React 18** with TypeScript
- **Material-UI (MUI)** for components
- **Recharts** for data visualization
- **WebSocket** client for real-time alerts
- Full **WCAG 2.2 AA** accessibility compliance

### Data Layer
- **Apache Kafka**: Event streaming (aiokafka client)
- **Azure Cosmos DB**: NoSQL document storage (azure-cosmos SDK)
- **Redis** (optional): Caching layer

### Observability
- **Prometheus**: Metrics collection
- **Grafana**: Dashboards and visualization
- **Jaeger**: Distributed tracing
- **OpenTelemetry**: Instrumentation

### DevOps
- **Docker**: Containerization
- **Kubernetes**: Orchestration (AKS, EKS, GKE)
- **GitHub Actions**: CI/CD
- **Helm** (optional): Package management

## 🚀 Quick Start

### Prerequisites

- **Docker** 20.10+
- **Docker Compose** 2.0+
- **kubectl** 1.24+
- **Node.js** 18+ (for frontend development)
- **Python** 3.11+

### Local Development with Docker Compose

1. **Clone the repository**
```bash
git clone <repository-url>
cd SMART-RETAIL-ALERT-MONITORING-PLATFORM
```

2. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. **Start all services**
```bash
docker-compose up -d
```

4. **Access the application**
- Frontend: http://localhost:3000
- API Gateway: http://localhost:8000
- Grafana: http://localhost:3001 (admin/admin)
- Jaeger UI: http://localhost:16686
- Kafka UI: http://localhost:8080

### Running Individual Services (Development)

#### Backend Service Example
```bash
cd services/api-gateway
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

#### Frontend
```bash
cd frontend
npm install
npm start
```

## 📦 Deployment

### Kubernetes Deployment

1. **Create namespace**
```bash
kubectl create namespace smart-retail
```

2. **Configure secrets**
```bash
kubectl create secret generic cosmos-db-secret \
  --from-literal=connection-string='your-cosmos-connection-string' \
  -n smart-retail

kubectl create secret generic jwt-secret \
  --from-literal=secret-key='your-jwt-secret-key' \
  -n smart-retail
```

3. **Deploy services**
```bash
kubectl apply -f infrastructure/kubernetes/
```

## 🏗️ Project Structure

```
.
├── frontend/                          # React TypeScript application
│   ├── public/
│   ├── src/
│   │   ├── components/               # React components
│   │   ├── pages/                    # Page components
│   │   ├── services/                 # API clients
│   │   └── types/                    # TypeScript types
│   ├── package.json
│   └── Dockerfile
│
├── services/                          # Backend microservices
│   ├── api-gateway/
│   ├── event-ingestion/
│   ├── alert-rules-engine/
│   ├── query-analytics/
│   └── user-management/
│
├── infrastructure/
│   ├── kubernetes/                   # K8s manifests
│   └── grafana/                      # Grafana dashboards
│
├── .github/
│   └── workflows/                    # GitHub Actions
│
├── docker-compose.yml
└── README.md
```

## 🚀 Deployment Guide for Live Demo

To deploy this for a live link on your resume:

### Option 1: Free Tier Deployment (Recommended for Resume)

**Using Render.com (Free tier available):**
1. Sign up at render.com
2. Connect your GitHub repository
3. Deploy each service as a Web Service
4. Use managed PostgreSQL instead of Cosmos DB
5. Use managed Redis for Kafka alternative

**Using Railway.app:**
1. Sign up at railway.app
2. Deploy from GitHub
3. Automatic HTTPS and custom domains
4. $5 free credit monthly

**Using Fly.io:**
1. Install flyctl CLI
2. Run `fly launch` in each service directory
3. Free tier includes 3 shared VMs

### Option 2: Cloud Platform (Production)

**Azure (Full stack):**
- AKS cluster
- Azure Cosmos DB
- Azure Event Hubs (Kafka-compatible)
- Estimated cost: $200-300/month

**AWS:**
- EKS cluster
- DynamoDB / DocumentDB
- Amazon MSK (Managed Kafka)
- Estimated cost: $180-250/month

## 📄 License

MIT License - see LICENSE file for details.

---

**⭐ Star this project if you find it useful!**
