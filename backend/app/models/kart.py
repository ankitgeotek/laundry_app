# app/models/kart.py
"""
Kart Model.

Represents an item in a user's shopping cart ("kart"). Each entry associates a user with a service,
the quantity selected, and any custom instructions.
"""

from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from .base import Base

class Kart(Base):
    __tablename__ = "kart"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    service_id = Column(Integer, ForeignKey("services.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    custom_instructions = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships:
    user = relationship("User", back_populates="kart_items")
    service = relationship("Service")  # You can add back_populates on the Service model if needed.
