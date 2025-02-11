# app/routes/service_routes.py
"""
Service Routes.

Defines the API endpoints for CRUD operations on laundry services.
Uses the ServiceResponseSchema to serialize Service objects.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.validators.service_validator import ServiceCreateSchema, ServiceUpdateSchema, ServiceResponseSchema
from app.controllers.service_controller import (
    create_service,
    get_service_by_id,
    get_all_services,
    update_service,
    delete_service
)
from typing import List

router = APIRouter(prefix="/services", tags=["Services"])

@router.post("/", response_model=ServiceResponseSchema)
async def add_service(service: ServiceCreateSchema, db: Session = Depends(get_db)):
    """
    Add a new service.
    
    Args:
      - service (ServiceCreateSchema): Data for the new service.
      - db (Session): Database session dependency.
    
    Returns:
      - ServiceResponseSchema: The created service data.
    """
    new_service = create_service(db, service)
    return new_service

@router.get("/{service_id}", response_model=ServiceResponseSchema)
async def read_service(service_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a service by its ID.
    
    Args:
      - service_id (int): The service ID.
      - db (Session): Database session dependency.
    
    Returns:
      - ServiceResponseSchema: The service data.
    """
    service = get_service_by_id(db, service_id)
    return service

@router.get("/", response_model=List[ServiceResponseSchema])
async def read_all_services(db: Session = Depends(get_db)):
    """
    Retrieve all services.
    
    Args:
      - db (Session): Database session dependency.
    
    Returns:
      - List[ServiceResponseSchema]: A list of all services.
    """
    services = get_all_services(db)
    return services

@router.put("/{service_id}", response_model=ServiceResponseSchema)
async def modify_service(service_id: int, service: ServiceUpdateSchema, db: Session = Depends(get_db)):
    """
    Update an existing service.
    
    Args:
      - service_id (int): The service ID.
      - service (ServiceUpdateSchema): Data to update the service.
      - db (Session): Database session dependency.
    
    Returns:
      - ServiceResponseSchema: The updated service data.
    """
    updated_service = update_service(db, service_id, service)
    return updated_service

@router.delete("/{service_id}", response_model=dict)
async def remove_service(service_id: int, db: Session = Depends(get_db)):
    """
    Delete a service.
    
    Args:
      - service_id (int): The service ID.
      - db (Session): Database session dependency.
    
    Returns:
      - dict: A confirmation message.
    """
    return delete_service(db, service_id)
