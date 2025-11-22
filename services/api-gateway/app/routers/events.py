from fastapi import APIRouter, HTTPException, Query, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import httpx
import logging

from ..models.events import EventCreate, Event, EventResponse
from ..config import settings

router = APIRouter()
security = HTTPBearer()
logger = logging.getLogger(__name__)


@router.post("/", response_model=Event, status_code=201)
async def create_event(
    event: EventCreate,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Create a new event"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{settings.event_ingestion_url}/events",
                json=event.model_dump(),
                headers={"Authorization": f"Bearer {credentials.credentials}"},
                timeout=10.0
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Event creation failed: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        logger.error(f"Error creating event: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/", response_model=EventResponse)
async def get_events(
    service: str = Query(None, description="Filter by service name"),
    from_timestamp: int = Query(None, description="Start timestamp"),
    to_timestamp: int = Query(None, description="End timestamp"),
    status: str = Query(None, description="Filter by status"),
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000),
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Get events with filters"""
    try:
        params = {
            "page": page,
            "page_size": page_size
        }
        if service:
            params["service"] = service
        if from_timestamp:
            params["from_timestamp"] = from_timestamp
        if to_timestamp:
            params["to_timestamp"] = to_timestamp
        if status:
            params["status"] = status
            
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.query_analytics_url}/events",
                params=params,
                headers={"Authorization": f"Bearer {credentials.credentials}"},
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Get events failed: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        logger.error(f"Error getting events: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/{event_id}", response_model=Event)
async def get_event(
    event_id: str,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Get a specific event by ID"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.query_analytics_url}/events/{event_id}",
                headers={"Authorization": f"Bearer {credentials.credentials}"},
                timeout=10.0
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Get event failed: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        logger.error(f"Error getting event: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
