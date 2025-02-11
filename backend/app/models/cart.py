"""
app/models/cart.py

Cart Model.

Represents an item in a user's shopping cart. Each record associates a user with a service,
the selected quantity, and any custom instructions.
"""

from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from .base import Base

class Cart(Base):
    __tablename__ = "cart"  # Consistently use "cart" instead of "kart"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    service_id = Column(Integer, ForeignKey("services.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    custom_instructions = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships: each cart item is linked to a user and a service.
    user = relationship("User", back_populates="cart_items")
    service = relationship("Service")

    def __repr__(self):
        return f"<Cart(id={self.id}, service_id={self.service_id}, user_id={self.user_id})>"
