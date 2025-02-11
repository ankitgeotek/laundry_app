# app/routes/user_routes.py
from app.utils.logger import logger, log_time_taken
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.controllers.user_controller import create_user_controller, authenticate_user_controller
from app.validators.user_validator import UserCreateSchema, UserLoginSchema
from app.database import get_db

"""
User routes module.

Defines FastAPI endpoints for user registration, login, and profile retrieval.
"""

logger.debug("User routes module loaded")

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup", response_model=dict)
async def signup(user: UserCreateSchema, db: Session = Depends(get_db)):
    """
    Endpoint for user registration (sign-up).

    Args:
        user (UserCreateSchema): User registration data.
        db (Session): Database session provided by dependency.
    Returns:
        dict: Message and user details upon successful registration.
    """
    new_user = create_user_controller(user, db)
    logger.debug("Signup successful for user: %s", new_user.email)
    return {
        "message": "User created successfully",
        "user": {"id": new_user.id, "name": new_user.name, "email": new_user.email}
    }

@router.post("/login", response_model=dict)
async def login(user: UserLoginSchema, db: Session = Depends(get_db)):
    """
    Endpoint for user login.

    Args:
        user (UserLoginSchema): User login credentials.
        db (Session): Database session provided by dependency.
    Returns:
        dict: JWT token and user details if login is successful.
    """
    auth_result = authenticate_user_controller(user, db)
    logger.debug("Login successful for user: %s", user.email)
    return auth_result

@router.get("/profile", response_model=dict)
async def get_profile(request: Request, db: Session = Depends(get_db)):
    """
    Protected endpoint to retrieve the current user's profile.
    
    Assumes that the JWT middleware attaches the user id to request.state.user.

    Args:
        request (Request): The incoming HTTP request.
        db (Session): Database session provided by dependency.
    Returns:
        dict: The authenticated user's profile.
    Raises:
        HTTPException: If the user is not found.
    """
    user_id = request.state.user
    from app.models.user import User  # Local import to avoid circular dependencies.
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        logger.error("User not found with id: %s", user_id)
        raise HTTPException(status_code=404, detail="User not found")
    logger.debug("Profile retrieved for user id: %s", user_id)
    return {"id": user.id, "name": user.name, "email": user.email}
