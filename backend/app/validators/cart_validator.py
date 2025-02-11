# app/validators/cart_validator.py
"""
Cart Validators.

Defines Pydantic schemas for creating, updating, and serializing cart items.
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.validators.service_validator import ServiceResponseSchema

class CartCreateSchema(BaseModel):
    """
    Schema for adding an item to the cart.
    """
    service_id: int = Field(..., description="ID of the service to add")
    quantity: int = Field(1, gt=0, description="Quantity of the service to add")
    custom_instructions: Optional[str] = Field(None, description="Custom instructions (optional)")

    class Config:
        orm_mode = True

class CartUpdateSchema(BaseModel):
    """
    Schema for updating an existing cart item.
    """
    quantity: Optional[int] = Field(None, gt=0, description="Updated quantity")
    custom_instructions: Optional[str] = Field(None, description="Updated custom instructions")

    class Config:
        orm_mode = True

class CartResponseSchema(BaseModel):
    """
    Schema for serializing a cart item.
    """
    id: int
    service_id: int
    quantity: int
    custom_instructions: Optional[str] = None
    created_at: datetime
    service: Optional[ServiceResponseSchema] = None  # Nested service details

    class Config:
        orm_mode = True
