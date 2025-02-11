# app/routes/kart_routes.py
"""
Kart Routes.

Defines API endpoints for managing kart items:
- Add an item to the kart.
- Retrieve all items for the authenticated user.
- Update a kart item.
- Delete a kart item.
"""

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.validators.kart_validator import KartCreateSchema, KartUpdateSchema, KartResponseSchema
from app.controllers.kart_controller import add_item_to_kart, get_kart_items, update_kart_item, delete_kart_item

router = APIRouter(prefix="/kart", tags=["Kart"])

@router.post("/", response_model=KartResponseSchema)
async def add_item(kart_data: KartCreateSchema, request: Request, db: Session = Depends(get_db)):
    """
    Add a new item to the authenticated user's kart.
    
    The user_id is derived from the JWT middleware attached to request.state.user.
    """
    user_id = request.state.user
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    item = add_item_to_kart(db, int(user_id), kart_data)
    return item

@router.get("/", response_model=List[KartResponseSchema])
async def read_kart(request: Request, db: Session = Depends(get_db)):
    """
    Retrieve all kart items for the authenticated user.
    """
    user_id = request.state.user
    if not user_id:
        raise HTTPException(status_code=401, detail="User not authenticated")
    items = get_kart_items(db, int(user_id))
    return items

@router.put("/{item_id}", response_model=KartResponseSchema)
async def update_item(item_id: int, kart_data: KartUpdateSchema, db: Session = Depends(get_db)):
    """
    Update an existing kart item.
    """
    updated_item = update_kart_item(db, item_id, kart_data)
    return updated_item

@router.delete("/{item_id}", response_model=dict)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    Delete a kart item.
    """
    return delete_kart_item(db, item_id)
