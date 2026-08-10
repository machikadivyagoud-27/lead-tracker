from datetime import datetime

from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    property_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    source: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    budget: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="new",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now
    )