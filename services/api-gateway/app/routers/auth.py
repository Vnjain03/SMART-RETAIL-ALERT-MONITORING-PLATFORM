from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import httpx
import logging

from ..models.auth import UserLogin, UserCreate, Token, User
from ..config import settings

router = APIRouter()
security = HTTPBearer()
logger = logging.getLogger(__name__)


@router.post("/register", response_model=User, status_code=201)
async def register(user_data: UserCreate):
    """Register a new user"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{settings.user_management_url}/auth/register",
                json=user_data.model_dump(),
                timeout=10.0
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"User registration failed: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
    except Exception as e:
        logger.error(f"Error during registration: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/login", response_model=Token)
async def login(credentials: UserLogin):
    """Login and get access token"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{settings.user_management_url}/auth/login",
                json=credentials.model_dump(),
                timeout=10.0
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Login failed: {e}")
        raise HTTPException(
            status_code=e.response.status_code,
            detail="Invalid credentials"
        )
    except Exception as e:
        logger.error(f"Error during login: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/me", response_model=User)
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Get current user info"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.user_management_url}/auth/me",
                headers={"Authorization": f"Bearer {credentials.credentials}"},
                timeout=10.0
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"Get user failed: {e}")
        raise HTTPException(
            status_code=e.response.status_code,
            detail="Unauthorized"
        )
    except Exception as e:
        logger.error(f"Error getting user: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
