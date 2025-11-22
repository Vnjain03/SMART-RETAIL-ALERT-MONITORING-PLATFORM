from fastapi import FastAPI
import logging

app = FastAPI(title="Alert Rules Engine")

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/rules")
async def get_rules():
    return []

@app.post("/rules")
async def create_rule(rule: dict):
    return {"id": "rule-123", **rule}
