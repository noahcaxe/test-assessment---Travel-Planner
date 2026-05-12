from datetime import datetime
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
)
from app.db.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    projects = relationship(
        "TravelProject",
        back_populates="user",
        cascade="all, delete-orphan",
    )
