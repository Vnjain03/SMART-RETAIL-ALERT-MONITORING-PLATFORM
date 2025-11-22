from pydantic import BaseModel
from typing import Optional, Dict, Any
from enum import Enum


class EventStatus(str, Enum):
    OK = "OK"
    ERROR = "ERROR"
    WARNING = "WARNING"


class EventCreate(BaseModel):
    service: str
    timestamp: int
    latency_ms: Optional[float] = None
    error_code: Optional[str] = None
    status: EventStatus = EventStatus.OK
    metadata: Optional[Dict[str, Any]] = None


class Event(EventCreate):
    id: str
    
    class Config:
        from_attributes = True


class EventResponse(BaseModel):
    events: list[Event]
    total: int
    page: int
    page_size: int
