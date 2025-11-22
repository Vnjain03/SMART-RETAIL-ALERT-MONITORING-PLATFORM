from fastapi import APIRouter
from typing import Dict

router = APIRouter()


@router.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "api-gateway"
    }


@router.get("/ready")
async def readiness_check() -> Dict[str, str]:
    """Readiness check endpoint"""
    return {
        "status": "ready",
        "service": "api-gateway"
    }
