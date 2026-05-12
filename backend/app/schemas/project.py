from datetime import date, datetime
import uuid
from pydantic import BaseModel, ConfigDict, Field

from app.schemas.project_place import (
    ProjectPlaceCreate,
    ProjectPlaceResponse,
)


class TravelProjectCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)

    description: str | None = None

    start_date: date | None = None

    places: list[ProjectPlaceCreate] = []


class TravelProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    start_date: date | None = None


class TravelProjectResponse(BaseModel):
    id: uuid

    user_id: uuid

    name: str
    description: str | None = None
    start_date: date | None = None

    created_at: datetime
    updated_at: datetime

    places: list[ProjectPlaceResponse]

    model_config = ConfigDict(from_attributes=True)