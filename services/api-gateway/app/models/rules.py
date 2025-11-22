from pydantic import BaseModel
from typing import Optional, Dict, Any
from enum import Enum


class RuleType(str, Enum):
    THRESHOLD = "THRESHOLD"
    RATE = "RATE"
    ANOMALY = "ANOMALY"


class RuleCondition(BaseModel):
    metric: str
    operator: str
    value: float
    consecutive_events: Optional[int] = None
    time_window_seconds: Optional[int] = None
    threshold_std_dev: Optional[float] = None
    lookback_minutes: Optional[int] = None


class RuleCreate(BaseModel):
    service: str
    name: str
    type: RuleType
    condition: RuleCondition
    severity: str
    enabled: bool = True
    description: Optional[str] = None


class Rule(RuleCreate):
    id: str
    created_at: int
    updated_at: Optional[int] = None
    
    class Config:
        from_attributes = True
