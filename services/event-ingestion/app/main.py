from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import make_asgi_app, Counter, Histogram
import logging
from pythonjsonlogger import jsonlogger

from .config import settings
from .models import EventCreate, Event, EventResponse
from .kafka_producer import kafka_producer

# Configure structured logging
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(logHandler)
logger.setLevel(settings.log_level.upper())

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="Event Ingestion Service for Smart Retail Platform",
)

# Prometheus metrics
EVENTS_INGESTED = Counter(
    "events_ingested_total",
    "Total events ingested",
    ["service", "status"]
)

INGESTION_DURATION = Histogram(
    "event_ingestion_duration_seconds",
    "Event ingestion duration",
    ["service"]
)


@app.on_event("startup")
async def startup_event():
    logger.info("Starting Event Ingestion Service")
    await kafka_producer.start()


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down Event Ingestion Service")
    await kafka_producer.stop()


@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "event-ingestion"}


@app.post("/events", response_model=EventResponse, status_code=201)
async def ingest_event(event_create: EventCreate):
    """Ingest an event and publish to Kafka"""
    try:
        # Create event with ID
        event = Event.from_create(event_create)
        
        # Send to Kafka
        await kafka_producer.send_event(
            topic=settings.kafka_topic_events,
            event=event.model_dump(),
            key=event.service  # Partition by service name
        )
        
        # Update metrics
        EVENTS_INGESTED.labels(
            service=event.service,
            status=event.status.value
        ).inc()
        
        logger.info(
            "Event ingested",
            extra={
                "event_id": event.id,
                "service": event.service,
                "status": event.status.value
            }
        )
        
        return EventResponse(
            id=event.id,
            status="success",
            message="Event ingested successfully"
        )
        
    except Exception as e:
        logger.error(f"Error ingesting event: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# Mount Prometheus metrics endpoint
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)
