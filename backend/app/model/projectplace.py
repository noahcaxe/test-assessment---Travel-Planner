from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    UniqueConstraint,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from app.db.database import Base 
from sqlalchemy.orm import relationship

class ProjectPlace(Base):
    __tablename__ = "project_places"

    id = Column(Integer, primary_key=True)

    project_id = Column(
        Integer,
        ForeignKey("travel_projects.id", ondelete="CASCADE"),
        nullable=False,
    )

    # external API
    external_id = Column(Integer, nullable=False)

    title = Column(String(255), nullable=False)
    artist = Column(String(255))
    image_url = Column(String(500))

    # local fields
    notes = Column(Text)
    visited = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    project = relationship(
        "TravelProject",
        back_populates="places",
    )

    __table_args__ = (
        UniqueConstraint(
            "project_id",
            "external_id",
            name="uq_project_external_place",
        ),
    )