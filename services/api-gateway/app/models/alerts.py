from pydantic import BaseModel
from typing import Optional
from enum import Enum


class AlertSeverity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class AlertCreate(BaseModel):
    service: str
    rule_id: str
    severity: AlertSeverity
    message: str
    timestamp: int
    metadata: Optional[dict] = None


class Alert(AlertCreate):
    id: str
    acknowledged: bool = False
    acknowledged_by: Optional[str] = None
    acknowledged_at: Optional[int] = None
    
    class Config:
        from_attributes = True


class AlertResponse(BaseModel):
    alerts: list[Alert]
    total: int
    page: int
    page_size: int
