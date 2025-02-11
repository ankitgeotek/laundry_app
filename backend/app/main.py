# app/main.py
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from app.routes.user_routes import router as user_router
from app.routes.service_routes import router as service_router
from app.routes.kart_routes import router as kart_router
from app.middleware.jwt_middleware import JWTMiddleware

"""
Main application entry point.

Initializes the FastAPI app, sets up middleware (CORS and JWT), and includes
user authentication routes. Also customizes the OpenAPI schema to include a
JWT security scheme so that you can manually add the token via Swagger's
'Authorize' button.
"""

logging.basicConfig(level=logging.DEBUG)
logging.debug("Starting FastAPI application with JWT security")

app = FastAPI(
    title="Laundry Service API",
    description="API for managing laundry services with JWT Authentication",
    version="1.0.0"
)

# Configure CORS middleware; adjust allowed origins in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, set to specific origins.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add the JWT middleware to enforce token validation on incoming requests.
app.add_middleware(JWTMiddleware)


app.include_router(user_router) # Include user authentication and profile endpoints.
app.include_router(service_router) # Include services endpoints.
app.include_router(kart_router) # Include kart endpoints.


def custom_openapi():
    """
    Generate a custom OpenAPI schema that includes a security scheme for JWT.
    
    This will add a 'bearerAuth' scheme to the OpenAPI components and
    apply it to all routes, which makes Swagger display an "Authorize" button.
    """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    # Define the security scheme for JWT (Bearer token)
    openapi_schema["components"]["securitySchemes"] = {
        "bearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "Enter your JWT token as: Bearer <token>"
        }
    }
    # Apply the security scheme to all endpoints (you can customize this per endpoint if desired)
    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            # Add security requirement only if the endpoint is not public (adjust as needed)
            openapi_schema["paths"][path][method]["security"] = [{"bearerAuth": []}]
    app.openapi_schema = openapi_schema
    logging.debug("Custom OpenAPI schema generated with JWT security")
    return app.openapi_schema

# Override the default OpenAPI schema with our custom version.
app.openapi = custom_openapi

if __name__ == "__main__":
    import uvicorn
    logging.debug("Running application via Uvicorn")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
