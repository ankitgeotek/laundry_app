# app/validators/kart_validator.py
"""
Kart Validators.

Defines Pydantic schemas for creating, updating, and serializing kart items.
"""

from pydantic import BaseModel, Field
from typing import Optional

class KartCreateSchema(BaseModel):
    """
    Schema for adding an item to the kart.

    Attributes:
      - service_id: The ID of the service to add.
      - quantity: The quantity of the service (must be > 0).
      - custom_instructions: Any custom instructions for this service (optional).
    """
    service_id: int = Field(..., description="ID of the service to add")
    quantity: int = Field(1, gt=0, description="Quantity of the service to add")
    custom_instructions: Optional[str] = Field(None, description="Custom instructions (optional)")

    class Config:
        orm_mode = True

class KartUpdateSchema(BaseModel):
    """
    Schema for updating a kart item.

    All fields are optional to support partial updates.
    """
    quantity: Optional[int] = Field(None, gt=0, description="Updated quantity")
    custom_instructions: Optional[str] = Field(None, description="Updated custom instructions")

    class Config:
        orm_mode = True

class KartResponseSchema(BaseModel):
    """
    Schema for serializing a kart item.

    Attributes:
      - id: The kart item ID.
      - service_id: The ID of the service.
      - quantity: The quantity selected.
      - custom_instructions: Custom instructions, if any.
    """
    id: int
    service_id: int
    quantity: int
    custom_instructions: Optional[str]

    class Config:
        orm_mode = True
