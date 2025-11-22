from fastapi import FastAPI, Query

app = FastAPI(title="Query & Analytics Service")

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/events")
async def get_events(page: int = 1, page_size: int = 100):
    return {"events": [], "total": 0, "page": page, "page_size": page_size}

@app.get("/alerts")
async def get_alerts(page: int = 1, page_size: int = 100):
    return {"alerts": [], "total": 0, "page": page, "page_size": page_size}
