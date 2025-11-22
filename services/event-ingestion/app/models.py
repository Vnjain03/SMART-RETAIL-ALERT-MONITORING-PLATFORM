from pydantic import BaseModel
from typing import Optional, Dict, Any
from enum import Enum
import time
import uuid


class EventStatus(str, Enum):
    OK = "OK"
    ERROR = "ERROR"
    WARNING = "WARNING"


class EventCreate(BaseModel):
    service: str
    timestamp: Optional[int] = None
    latency_ms: Optional[float] = None
    error_code: Optional[str] = None
    status: EventStatus = EventStatus.OK
    metadata: Optional[Dict[str, Any]] = None
    
    def model_post_init(self, __context):
        if self.timestamp is None:
            self.timestamp = int(time.time())


class Event(EventCreate):
    id: str
    
    @classmethod
    def from_create(cls, event_create: EventCreate):
        return cls(
            id=str(uuid.uuid4()),
            service=event_create.service,
            timestamp=event_create.timestamp or int(time.time()),
            latency_ms=event_create.latency_ms,
            error_code=event_create.error_code,
            status=event_create.status,
            metadata=event_create.metadata
        )


class EventResponse(BaseModel):
    id: str
    status: str
    message: str
