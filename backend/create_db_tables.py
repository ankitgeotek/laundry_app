# backend/create_db_tables.py
from sqlalchemy import create_engine
from app.models import Base
from app.config import DATABASE_URL

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Please define it in your environment.")

engine = create_engine(DATABASE_URL)

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()