# app/validators/user_validator.py
import logging
from pydantic import BaseModel, EmailStr, Field

"""
User validators module.

Defines Pydantic models for validating user registration and login requests.
"""

logging.debug("Loading user validator schemas")

class UserCreateSchema(BaseModel):
    """
    Schema for user registration (sign-up).

    Attributes:
        name: User's full name.
        email: Valid email address.
        password: Password (minimum 6 characters).
        phone: Optional phone number.
        address: Optional address.
    """
    name: str = Field(..., min_length=1, description="User's full name")
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., min_length=6, description="User's password (min 6 characters)")
    phone: str = None
    address: str = None

    class Config:
        orm_mode = True

class UserLoginSchema(BaseModel):
    """
    Schema for user login.

    Attributes:
        email: User's email address.
        password: User's password.
    """
    email: EmailStr = Field(..., description="User's email address")
    password: str = Field(..., min_length=6, description="User's password")
