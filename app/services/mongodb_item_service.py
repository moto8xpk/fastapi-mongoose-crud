# app/services/mongodb_item_service.py

from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import List
from models.item import Item, ItemInDB
from services.item_service import AbstractItemService


class MongoDBItemService(AbstractItemService):

    def __init__(self, db_url: str, db_name: str):
        self.client = AsyncIOMotorClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db.fastapi_collection

    def item_serializer(self, item) -> dict:
        return {
            "id": str(item["_id"]),
            "name": item["name"],
            "description": item.get("description"),
            "price": item["price"],
            "tax": item.get("tax"),
        }

    async def create_item(self, item: Item) -> ItemInDB:
        result = await self.collection.insert_one(item.dict())
        return ItemInDB(id=str(result.inserted_id), **item.dict())

    async def get_items(self, skip: int = 0, limit: int = 10) -> List[ItemInDB]:
        items = await self.collection.find().skip(skip).limit(limit).to_list(length=limit)
        return [self.item_serializer(item) for item in items]

    async def get_item(self, item_id: str) -> ItemInDB:
        item = await self.collection.find_one({"_id": ObjectId(item_id)})
        if item:
            return self.item_serializer(item)
        return None

    async def update_item(self, item_id: str, item: Item) -> ItemInDB:
        result = await self.collection.update_one({"_id": ObjectId(item_id)}, {"$set": item.dict()})
        if result.modified_count == 1:
            return ItemInDB(id=item_id, **item.dict())
        return None

    async def delete_item(self, item_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(item_id)})
        return result.deleted_count == 1
