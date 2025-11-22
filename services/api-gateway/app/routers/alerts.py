from fastapi import APIRouter, HTTPException, Query, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import httpx
import logging

from ..models.alerts import Alert, AlertResponse
from ..config import settings

router = APIRouter()
security = HTTPBearer()
logger = logging.getLogger(__name__)


@router.get("/", response_model=AlertResponse)
async def get_alerts(
    service: str = Query(None, description="Filter by service name"),
    severity: str = Query(None, description="Filter by severity"),
    acknowledged: bool = Query(None, description="Filter by acknowledged status"),
    from_timestamp: int = Query(None, description="Start timestamp"),
    to_timestamp: int = Query(None, description="End timestamp"),
    page: int = Query(1, ge=1),
    page_size: int = Query(100, ge=1, le=1000),
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Get alerts with filters"""
    try:
        params = {
            "page": page,
            "page_size": page_size
        }
        if service:
            params["service"] = service
        if severity:
            params["severity"] = severity
        if acknowledged is not None:
            params["acknowledged"] = acknowledged
        if from_timestamp:
            params["from_timestamp"] = from_timestamp
        if to_timestamp:
            params["to_timestamp"] = to_timestamp
            
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.query_analytics_url}/alerts",
                params=params,
                headers={"Authorization": f"Bearer {credentials.credentials}"},
                timeout=30.0
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Get alerts failed: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        logger.error(f"Error getting alerts: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/{alert_id}", response_model=Alert)
async def get_alert(
    alert_id: str,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Get a specific alert by ID"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.query_analytics_url}/alerts/{alert_id}",
                headers={"Authorization": f"Bearer {credentials.credentials}"},
                timeout=10.0
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Get alert failed: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        logger.error(f"Error getting alert: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.patch("/{alert_id}/acknowledge")
async def acknowledge_alert(
    alert_id: str,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Acknowledge an alert"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.patch(
                f"{settings.query_analytics_url}/alerts/{alert_id}/acknowledge",
                headers={"Authorization": f"Bearer {credentials.credentials}"},
                timeout=10.0
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Acknowledge alert failed: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        logger.error(f"Error acknowledging alert: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
