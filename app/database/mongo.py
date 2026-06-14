from pymongo import MongoClient
from pymongo.database import Database
from app.core.config import MONGO_URI, DATABASE_NAME

client: MongoClient = MongoClient(MONGO_URI)

def get_database() -> Database:
    """
    Retorna la base de datos configurada.

    :return: Instancia de la base de datos.
    """
    return client[DATABASE_NAME]