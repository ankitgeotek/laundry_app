# app/utils/jwt_utils.py
import logging
from datetime import datetime, timedelta
from jose import jwt
from app.config import JWT_SECRET_KEY, ALGORITHM

"""
JWT utility module.

Provides functions for creating JWT access tokens.
"""

logging.debug("JWT utilities module loaded")

def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    Create a JWT access token.

    Args:
        data (dict): Data to include in the token payload.
        expires_delta (timedelta, optional): Token expiration duration. Defaults to 15 minutes.
    Returns:
        str: The encoded JWT token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    logging.debug("Access token created; expires at %s", expire)
    return encoded_jwt
