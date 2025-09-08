from pymongo import MongoClient
from settings import AppSettings

settings = AppSettings()

client = MongoClient(settings.DATABASE_URL)


try:
    client.admin.command('ping')
    print('Database connection successful')
except Exception as e:
    print(f'Database connection failed: {e}')

def get_db_connection():
    db = client.get_database(settings.DATABASE_NAME)
    return db




