# app/controllers/service_controller.py
"""
Service Controller.

Contains business logic for creating, reading, updating, and deleting laundry services.
Uses SQLAlchemy sessions and logs operations. Follows best practices for error handling.
"""

import logging
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.service import Service
from app.validators.service_validator import ServiceCreateSchema, ServiceUpdateSchema

logger = logging.getLogger("service_controller")

def create_service(db: Session, service_data: ServiceCreateSchema) -> Service:
    """
    Creates a new service in the database.
    
    Args:
        db (Session): The database session.
        service_data (ServiceCreateSchema): Data for the new service.
    
    Returns:
        Service: The created service object.
    
    Raises:
        HTTPException: If a service with the same name already exists.
    """
    existing_service = db.query(Service).filter(Service.name == service_data.name).first()
    if existing_service:
        logger.error("Service already exists with name: %s", service_data.name)
        raise HTTPException(status_code=400, detail="Service already exists")
    
    new_service = Service(**service_data.dict())
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    logger.info("Created service with id: %s", new_service.id)
    return new_service

def get_service_by_id(db: Session, service_id: int) -> Service:
    """
    Retrieves a service by its ID.
    
    Args:
        db (Session): The database session.
        service_id (int): ID of the service.
    
    Returns:
        Service: The service object.
    
    Raises:
        HTTPException: If the service is not found.
    """
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        logger.error("Service not found with id: %s", service_id)
        raise HTTPException(status_code=404, detail="Service not found")
    return service

def get_all_services(db: Session):
    """
    Retrieves all services from the database.
    
    Args:
        db (Session): The database session.
    
    Returns:
        List[Service]: A list of all services.
    """
    services = db.query(Service).all()
    logger.info("Retrieved %d services", len(services))
    return services

def update_service(db: Session, service_id: int, service_data: ServiceUpdateSchema) -> Service:
    """
    Updates an existing service.
    
    Args:
        db (Session): The database session.
        service_id (int): ID of the service to update.
        service_data (ServiceUpdateSchema): Data for updating the service.
    
    Returns:
        Service: The updated service object.
    
    Raises:
        HTTPException: If the service is not found.
    """
    service = get_service_by_id(db, service_id)
    update_data = service_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(service, key, value)
    db.commit()
    db.refresh(service)
    logger.info("Updated service with id: %s", service_id)
    return service

def delete_service(db: Session, service_id: int):
    """
    Deletes a service from the database.
    
    Args:
        db (Session): The database session.
        service_id (int): ID of the service to delete.
    
    Returns:
        dict: A confirmation message.
    
    Raises:
        HTTPException: If the service is not found.
    """
    service = get_service_by_id(db, service_id)
    db.delete(service)
    db.commit()
    logger.info("Deleted service with id: %s", service_id)
    return {"detail": "Service deleted successfully"}
