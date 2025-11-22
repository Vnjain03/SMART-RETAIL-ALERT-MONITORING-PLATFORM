from pydantic import BaseModel, EmailStr
from typing import Optional


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int


class TokenData(BaseModel):
    email: Optional[str] = None
    user_id: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None
    role: str = "user"


class User(BaseModel):
    id: str
    email: EmailStr
    full_name: Optional[str] = None
    role: str
    is_active: bool = True
    created_at: int
    
    class Config:
        from_attributes = True
