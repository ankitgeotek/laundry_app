# app/utils/hashing.py
import logging
from passlib.context import CryptContext

"""
Hashing utility module.

Provides functions to hash passwords and verify plaintext passwords against their hashes.
"""

logging.debug("Initializing password hashing context")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hash a plaintext password using bcrypt.

    Args:
        password (str): The plaintext password.
    Returns:
        str: The hashed password.
    """
    hashed = pwd_context.hash(password)
    logging.debug("Password hashed successfully")
    return hashed

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plaintext password against a hashed password.

    Args:
        plain_password (str): The plaintext password.
        hashed_password (str): The hashed password.
    Returns:
        bool: True if the password matches, else False.
    """
    valid = pwd_context.verify(plain_password, hashed_password)
    logging.debug("Password verification result: %s", valid)
    return valid
