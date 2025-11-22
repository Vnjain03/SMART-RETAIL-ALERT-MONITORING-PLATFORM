from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

app = FastAPI(title="User Management Service")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/auth/register")
async def register(user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    return {
        "id": "user-123",
        "email": user.email,
        "role": "user",
        "created_at": int(datetime.now().timestamp())
    }

@app.post("/auth/login")
async def login(credentials: UserLogin):
    # Demo: accept any login
    token_data = {"sub": credentials.email, "exp": datetime.utcnow() + timedelta(hours=1)}
    access_token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer", "expires_in": 3600}

@app.get("/auth/me")
async def get_current_user():
    return {"id": "user-123", "email": "demo@example.com", "role": "admin"}
