"""
models.py — SQLModel database table definitions.
Phase II: Full-Stack Web App
"""
from datetime import datetime, date
from typing import Optional, List
from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import ARRAY, TEXT


class Task(SQLModel, table=True):
    """Database table for todo tasks."""

    __tablename__ = "tasks"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=500)
    status: str = Field(default="pending", max_length=20)
    priority: str = Field(default="medium", max_length=10)
    tags: Optional[List[str]] = Field(
        default=None,
        sa_column=Column(ARRAY(TEXT), nullable=True, server_default="{}"),
    )
    due_date: Optional[date] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
