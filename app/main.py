# app/main.py

from fastapi import FastAPI, HTTPException, Depends
from typing import List
from models.item import Item, ItemInDB
from services.item_factory import AbstractFactory, MongoDBFactory
from services.item_service import AbstractItemService

app = FastAPI()


# Dependency injection of the item service using the factory
def get_item_service(factory: AbstractFactory = Depends(MongoDBFactory)) -> AbstractItemService:
    return factory.create_item_service()


@app.post("/items/", response_model=ItemInDB)
async def create_item(item: Item, service: AbstractItemService = Depends(get_item_service)):
    created_item = await service.create_item(item)
    return created_item


@app.get("/items/", response_model=List[ItemInDB])
async def read_items(skip: int = 0, limit: int = 10, service: AbstractItemService = Depends(get_item_service)):
    items = await service.get_items(skip=skip, limit=limit)
    return items


@app.get("/items/{item_id}", response_model=ItemInDB)
async def read_item(item_id: str, service: AbstractItemService = Depends(get_item_service)):
    item = await service.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=ItemInDB)
async def update_item(item_id: str, item: Item, service: AbstractItemService = Depends(get_item_service)):
    updated_item = await service.update_item(item_id, item)
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item


@app.delete("/items/{item_id}")
async def delete_item(item_id: str, service: AbstractItemService = Depends(get_item_service)):
    success = await service.delete_item(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}
