# app/config.py
import os

"""
Configuration settings for the application.

This module retrieves configuration values (like JWT keys and algorithms)
from environment variables or provides default values.
"""

# Secret key for JWT encoding/decoding.
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_secret_key_here")

# JWT signing algorithm.
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

DATABASE_URL = "postgresql://ankitgeotek:sqlpassword@localhost:5432/laundry_db"
