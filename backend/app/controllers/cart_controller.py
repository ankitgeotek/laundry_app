# app/controllers/cart_controller.py
"""
Cart Controller.

Provides business logic for managing a user's cart.
"""

import logging
from sqlalchemy.orm import Session, joinedload
from fastapi import HTTPException
from app.models.cart import Cart
from app.validators.cart_validator import CartCreateSchema, CartUpdateSchema

logger = logging.getLogger("cart_controller")

def add_item_to_cart(db: Session, user_id: int, cart_data: CartCreateSchema) -> Cart:
    new_item = Cart(user_id=user_id, **cart_data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    logger.info("Added new cart item with id %s for user %s", new_item.id, user_id)
    return new_item

def get_cart_items(db: Session, user_id: int):
    # Use joinedload to eagerly load the related service
    items = db.query(Cart).options(joinedload(Cart.service)).filter(Cart.user_id == user_id).all()
    logger.info("Retrieved %d cart items for user %s", len(items), user_id)
    return items

def update_cart_item(db: Session, item_id: int, cart_data: CartUpdateSchema) -> Cart:
    item = db.query(Cart).filter(Cart.id == item_id).first()
    if not item:
        logger.error("Cart item not found with id %s", item_id)
        raise HTTPException(status_code=404, detail="Cart item not found")
    update_data = cart_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    logger.info("Updated cart item with id %s", item_id)
    return item

def delete_cart_item(db: Session, item_id: int):
    item = db.query(Cart).filter(Cart.id == item_id).first()
    if not item:
        logger.error("Cart item not found with id %s", item_id)
        raise HTTPException(status_code=404, detail="Cart item not found")
    db.delete(item)
    db.commit()
    logger.info("Deleted cart item with id %s", item_id)
    return {"detail": "Cart item deleted successfully"}

def clear_cart(db: Session, user_id: int):
    items = db.query(Cart).filter(Cart.user_id == user_id).all()
    for item in items:
        db.delete(item)
    db.commit()
    logger.info("Cleared all cart items for user %s", user_id)
    return {"detail": "Cart cleared successfully"}

def get_cart_total(db: Session, user_id: int) -> float:
    items = db.query(Cart).options(joinedload(Cart.service)).filter(Cart.user_id == user_id).all()
    total = 0.0
    for item in items:
        service = item.service
        if service:
            total += item.quantity * service.base_price
    logger.info("Calculated cart total for user %s: %f", user_id, total)
    return total
