# app/models/delivery.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from .base import Base

class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    staff_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # Assuming staff are part of the users table
    pickup_time = Column(DateTime)
    delivery_time = Column(DateTime)
    status = Column(String, nullable=False, default="Scheduled")  # e.g., "Scheduled", "In Transit", "Delivered"

    # Relationships
    order = relationship("Order", back_populates="delivery")
    staff = relationship("User")
