# app/controllers/user_controller.py
import logging
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.validators.user_validator import UserCreateSchema, UserLoginSchema
from app.utils.hashing import hash_password, verify_password
from app.utils.jwt_utils import create_access_token

"""
User controller module.

Contains business logic for creating a new user and authenticating an existing user.
"""

logging.debug("User controller module loaded")

def create_user_controller(user_data: UserCreateSchema, db: Session) -> User:
    """
    Create a new user in the database after checking for email uniqueness.

    Args:
        user_data (UserCreateSchema): Validated user registration data.
        db (Session): Database session.
    Returns:
        User: The newly created user object.
    Raises:
        HTTPException: If the email is already registered.
    """
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        logging.error("Email already registered: %s", user_data.email)
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pwd = hash_password(user_data.password)
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        password_hash=hashed_pwd,
        phone=user_data.phone,
        address=user_data.address,
        role="customer"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    logging.debug("Created new user with id: %s", new_user.id)
    return new_user

def authenticate_user_controller(user_data: UserLoginSchema, db: Session) -> dict:
    """
    Authenticate a user with email and password. If successful, return a JWT token.

    Args:
        user_data (UserLoginSchema): Validated user login data.
        db (Session): Database session.
    Returns:
        dict: A dictionary with JWT token and user details.
    Raises:
        HTTPException: If authentication fails.
    """
    user = db.query(User).filter(User.email == user_data.email).first()
    if not user or not verify_password(user_data.password, user.password_hash):
        logging.error("Authentication failed for email: %s", user_data.email)
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    access_token = create_access_token(data={"sub": str(user.id)})
    logging.debug("User authenticated; token generated for user id: %s", user.id)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {"id": user.id, "name": user.name, "email": user.email}
    }
