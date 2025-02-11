# app/validators/service_validator.py
"""
Service Validators.

Defines Pydantic schemas for creating, updating, and serializing laundry services.
"""

from pydantic import BaseModel, Field

class ServiceCreateSchema(BaseModel):
    """
    Schema for creating a new service.
    
    Attributes:
        name: Name of the service.
        description: Detailed description (optional).
        base_price: Base price for the service (must be > 0).
        category: Category of the service (optional).
        image_url: URL or path to the service image (optional).
    """
    name: str = Field(..., min_length=1, description="Name of the service")
    description: str = Field(None, description="Description of the service")
    base_price: float = Field(..., gt=0, description="Base price for the service")
    category: str = Field(None, description="Category for the service")
    image_url: str = Field(None, description="URL of the service image (optional)")

    class Config:
        orm_mode = True

class ServiceUpdateSchema(BaseModel):
    """
    Schema for updating an existing service.
    
    All fields are optional to support partial updates.
    """
    name: str = Field(None, min_length=1, description="Name of the service")
    description: str = Field(None, description="Description of the service")
    base_price: float = Field(None, gt=0, description="Base price for the service")
    category: str = Field(None, description="Category for the service")
    image_url: str = Field(None, description="URL of the service image (optional)")

    class Config:
        orm_mode = True

class ServiceResponseSchema(BaseModel):
    """
    Response schema for a service.
    
    This schema is used to serialize the Service model for API responses.
    """
    id: int
    name: str
    description: str = None
    base_price: float
    category: str = None
    image_url: str = None

    class Config:
        orm_mode = True
