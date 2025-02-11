# app/middleware/jwt_middleware.py

from app.utils.logger import logger, log_time_taken
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
from jose import jwt, JWTError
from app.config import JWT_SECRET_KEY, ALGORITHM

"""
JWT middleware module.

Intercepts incoming requests to validate the JWT token found in the Authorization header.
Exempts specified endpoints from validation and attaches the user id (from the token's "sub" claim)
to request.state.user.
"""

class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Define endpoints that do not require JWT authentication.
        excluded_paths = [
            "/docs",
            "/auth/login",
            "/auth/signup",
            "/openapi.json",
            "/generate/process-llm-response"
        ]

        # Skip JWT validation for OPTIONS requests or excluded paths.
        if request.method == "OPTIONS" or any(request.url.path.startswith(path) for path in excluded_paths):
            logger.info("Skipping JWT validation for path: %s, method: %s", request.url.path, request.method)
            return await call_next(request)

        # Retrieve the Authorization header.
        token = request.headers.get("Authorization")
        logger.debug("Received Authorization header: %s", token)
        if token is None or not token.startswith("Bearer "):
            logger.error("Missing or improperly formatted token: %s", token)
            raise HTTPException(status_code=401, detail="Token missing or invalid format")

        # Remove the "Bearer " prefix.
        token = token[len("Bearer "):]

        try:
            # Decode the token using the configured secret key and algorithm.
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
            logger.info("JWT decoded successfully: %s", payload)
            
            # Check if the 'sub' claim is present.
            if "sub" not in payload:
                logger.error("Token payload missing 'sub' claim: %s", payload)
                raise HTTPException(status_code=401, detail="Invalid token payload")
            
            # Attach the user id to the request state.
            request.state.user = payload["sub"]
            logger.debug("Set request.state.user to: %s", request.state.user)
        except JWTError as e:
            logger.error("JWT decoding error: %s", e)
            raise HTTPException(status_code=401, detail="Invalid token")

        # Continue processing the request.
        response = await call_next(request)
        return response
