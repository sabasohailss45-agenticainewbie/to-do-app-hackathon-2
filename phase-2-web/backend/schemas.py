"""
schemas.py — Pydantic request/response schemas.
Phase II: Full-Stack Web App
"""
from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel, field_validator


VALID_PRIORITIES = {"high", "medium", "low"}
VALID_STATUSES = {"pending", "completed"}


class TaskCreate(BaseModel):
    title: str
    priority: str = "medium"
    tags: List[str] = []
    due_date: Optional[date] = None

    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Title cannot be empty")
        return v

    @field_validator("priority")
    @classmethod
    def priority_valid(cls, v: str) -> str:
        v = v.lower().strip()
        if v not in VALID_PRIORITIES:
            raise ValueError(f"Priority must be one of: {', '.join(VALID_PRIORITIES)}")
        return v


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    tags: Optional[List[str]] = None
    due_date: Optional[date] = None

    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            v = v.strip()
            if not v:
                raise ValueError("Title cannot be empty")
        return v

    @field_validator("priority")
    @classmethod
    def priority_valid(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            v = v.lower().strip()
            if v not in VALID_PRIORITIES:
                raise ValueError(f"Priority must be one of: {', '.join(VALID_PRIORITIES)}")
        return v

    @field_validator("status")
    @classmethod
    def status_valid(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            v = v.lower().strip()
            if v not in VALID_STATUSES:
                raise ValueError(f"Status must be one of: {', '.join(VALID_STATUSES)}")
        return v


class TaskResponse(BaseModel):
    id: int
    title: str
    status: str
    priority: str
    tags: List[str]
    due_date: Optional[date]
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
