# app/controllers/kart_controller.py
"""
Kart Controller.

Provides business logic for managing the user's kart items:
- Add a new kart item.
- Retrieve all kart items for a user.
- Update a kart item (e.g., change quantity, custom instructions).
- Delete a kart item.

Each function uses proper error handling and logging.
"""

import logging
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.kart import Kart
from app.validators.kart_validator import KartCreateSchema, KartUpdateSchema

logger = logging.getLogger("kart_controller")

def add_item_to_kart(db: Session, user_id: int, kart_data: KartCreateSchema) -> Kart:
    """
    Adds a new item to the user's kart.

    Args:
      - db (Session): Database session.
      - user_id (int): The authenticated user's ID.
      - kart_data (KartCreateSchema): Data for the new kart item.

    Returns:
      - Kart: The newly created kart item.
    """
    new_item = Kart(user_id=user_id, **kart_data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    logger.info("Added new kart item with id: %s for user: %s", new_item.id, user_id)
    return new_item

def get_kart_items(db: Session, user_id: int):
    """
    Retrieves all kart items for a specific user.

    Args:
      - db (Session): Database session.
      - user_id (int): The user's ID.

    Returns:
      - List[Kart]: A list of kart items.
    """
    items = db.query(Kart).filter(Kart.user_id == user_id).all()
    logger.info("Retrieved %d kart items for user: %s", len(items), user_id)
    return items

def update_kart_item(db: Session, item_id: int, kart_data: KartUpdateSchema) -> Kart:
    """
    Updates an existing kart item.

    Args:
      - db (Session): Database session.
      - item_id (int): The ID of the kart item to update.
      - kart_data (KartUpdateSchema): Update data.

    Returns:
      - Kart: The updated kart item.

    Raises:
      - HTTPException: If the kart item is not found.
    """
    item = db.query(Kart).filter(Kart.id == item_id).first()
    if not item:
        logger.error("Kart item not found: %s", item_id)
        raise HTTPException(status_code=404, detail="Kart item not found")
    
    update_data = kart_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    logger.info("Updated kart item with id: %s", item_id)
    return item

def delete_kart_item(db: Session, item_id: int):
    """
    Deletes a kart item from the database.

    Args:
      - db (Session): Database session.
      - item_id (int): The ID of the kart item.

    Returns:
      - dict: Confirmation message.

    Raises:
      - HTTPException: If the kart item is not found.
    """
    item = db.query(Kart).filter(Kart.id == item_id).first()
    if not item:
        logger.error("Kart item not found: %s", item_id)
        raise HTTPException(status_code=404, detail="Kart item not found")
    db.delete(item)
    db.commit()
    logger.info("Deleted kart item with id: %s", item_id)
    return {"detail": "Kart item deleted successfully"}
