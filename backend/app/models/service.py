# app/models/service.py
"""
Service Model.

Defines the Service model representing a laundry service offering.
Each service has a name, description, base price, category, and an optional image URL.
Also includes a relationship to order items.
"""

from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import relationship
from .base import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    base_price = Column(Float, nullable=False)
    category = Column(String, nullable=True)  # Optional grouping field (e.g., "wash and fold", "dry clean")
    image_url = Column(String, nullable=True)   # URL or path to the service image

    # Relationship: One service may appear in many order items.
    order_items = relationship("OrderItem", back_populates="service", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Service(id={self.id}, name='{self.name}')>"
