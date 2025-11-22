from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import httpx
import logging

from ..models.rules import Rule, RuleCreate
from ..config import settings

router = APIRouter()
security = HTTPBearer()
logger = logging.getLogger(__name__)


@router.post("/", response_model=Rule, status_code=201)
async def create_rule(
    rule: RuleCreate,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Create a new alert rule"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{settings.alert_rules_engine_url}/rules",
                json=rule.model_dump(),
                headers={"Authorization": f"Bearer {credentials.credentials}"},
                timeout=10.0
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Rule creation failed: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        logger.error(f"Error creating rule: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/", response_model=list[Rule])
async def get_rules(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Get all alert rules"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.alert_rules_engine_url}/rules",
                headers={"Authorization": f"Bearer {credentials.credentials}"},
                timeout=10.0
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Get rules failed: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        logger.error(f"Error getting rules: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/{rule_id}", response_model=Rule)
async def get_rule(
    rule_id: str,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Get a specific rule by ID"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.alert_rules_engine_url}/rules/{rule_id}",
                headers={"Authorization": f"Bearer {credentials.credentials}"},
                timeout=10.0
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Get rule failed: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        logger.error(f"Error getting rule: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put("/{rule_id}", response_model=Rule)
async def update_rule(
    rule_id: str,
    rule: RuleCreate,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Update an alert rule"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(
                f"{settings.alert_rules_engine_url}/rules/{rule_id}",
                json=rule.model_dump(),
                headers={"Authorization": f"Bearer {credentials.credentials}"},
                timeout=10.0
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Update rule failed: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        logger.error(f"Error updating rule: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/{rule_id}", status_code=204)
async def delete_rule(
    rule_id: str,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """Delete an alert rule"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"{settings.alert_rules_engine_url}/rules/{rule_id}",
                headers={"Authorization": f"Bearer {credentials.credentials}"},
                timeout=10.0
            )
            response.raise_for_status()
            return None
    except httpx.HTTPStatusError as e:
        logger.error(f"Delete rule failed: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        logger.error(f"Error deleting rule: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
