# app/services/item_service.py

from abc import ABC, abstractmethod
from typing import List
from models.item import Item, ItemInDB


class AbstractItemService(ABC):

    @abstractmethod
    async def create_item(self, item: Item) -> ItemInDB:
        pass

    @abstractmethod
    async def get_items(self, skip: int = 0, limit: int = 10) -> List[ItemInDB]:
        pass

    @abstractmethod
    async def get_item(self, item_id: str) -> ItemInDB:
        pass

    @abstractmethod
    async def update_item(self, item_id: str, item: Item) -> ItemInDB:
        pass

    @abstractmethod
    async def delete_item(self, item_id: str) -> bool:
        pass
