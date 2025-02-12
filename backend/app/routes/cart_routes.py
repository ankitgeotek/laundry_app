# app/routes/cart_routes.py
"""
Cart Routes.

Defines API endpoints for managing cart items.
"""

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List, Dict
from app.database import get_db
from app.validators.cart_validator import CartCreateSchema, CartUpdateSchema, CartResponseSchema
from app.controllers.cart_controller import (
    add_item_to_cart,
    get_cart_items,
    update_cart_item,
    delete_cart_item,
    clear_cart,
    get_cart_total
)

router = APIRouter(prefix="/cart", tags=["Cart"])

@router.post("/", response_model=CartResponseSchema)
async def add_item(cart_data: CartCreateSchema, request: Request, db: Session = Depends(get_db)):
    user_id = request.state.user
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    item = add_item_to_cart(db, int(user_id), cart_data)
    return item

@router.get("/", response_model=List[CartResponseSchema])
async def read_cart(request: Request, db: Session = Depends(get_db)):
    user_id = request.state.user
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    items = get_cart_items(db, int(user_id))
    return items

@router.put("/{item_id}", response_model=CartResponseSchema)
async def update_item(item_id: int, cart_data: CartUpdateSchema, db: Session = Depends(get_db)):
    updated_item = update_cart_item(db, item_id, cart_data)
    return updated_item

@router.delete("/{item_id}", response_model=Dict[str, str])
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    return delete_cart_item(db, item_id)

@router.delete("/clear", response_model=Dict[str, str])
async def clear_all_items(request: Request, db: Session = Depends(get_db)):
    user_id = request.state.user
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    return clear_cart(db, int(user_id))

@router.get("/total", response_model=float)
async def cart_total(request: Request, db: Session = Depends(get_db)):
    user_id = request.state.user
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    total = get_cart_total(db, int(user_id))
    return total
