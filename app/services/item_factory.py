# app/services/item_factory.py

from abc import ABC, abstractmethod
from services.item_service import AbstractItemService
from services.mongodb_item_service import MongoDBItemService
from database import DATABASE_URL, DATABASE_NAME


class AbstractFactory(ABC):

    @abstractmethod
    def create_item_service(self) -> AbstractItemService:
        pass

class MongoDBFactory(AbstractFactory):

    def create_item_service(self) -> AbstractItemService:
        return MongoDBItemService(db_url=DATABASE_URL, db_name=DATABASE_NAME)
