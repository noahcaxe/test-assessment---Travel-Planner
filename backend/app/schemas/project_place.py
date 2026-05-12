import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProjectPlaceCreate(BaseModel):
    external_id: uuid.UUID


class ProjectPlaceUpdate(BaseModel):
    notes: str | None = None
    visited: bool | None = None


class ProjectPlaceResponse(BaseModel):
    id: uuid.UUID
    external_id: uuid.UUID

    title: str
    artist: str | None = None
    image_url: str | None = None

    notes: str | None = None
    visited: bool

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)