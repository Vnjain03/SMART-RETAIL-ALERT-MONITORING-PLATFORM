# Kubernetes Deployment Guide

## Prerequisites

1. Kubernetes cluster (v1.24+)
2. kubectl configured
3. Docker images pushed to a registry

## Quick Deploy

```bash
# Create namespace
kubectl apply -f namespace/namespace.yaml

# Create secrets (update with your values)
kubectl create secret generic jwt-secret \
  --from-literal=secret-key='your-secret-key' \
  -n smart-retail

kubectl create secret generic cosmos-db-secret \
  --from-literal=connection-string='your-cosmos-connection-string' \
  -n smart-retail

# Deploy all services
kubectl apply -f deployments/
kubectl apply -f services/
kubectl apply -f ingress/

# Check deployment status
kubectl get pods -n smart-retail
kubectl get services -n smart-retail
```

## Accessing the Application

After deployment, access via the Ingress endpoint or LoadBalancer IP.

## Monitoring

```bash
# View logs
kubectl logs -f deployment/api-gateway -n smart-retail

# Check metrics
kubectl top pods -n smart-retail
```
