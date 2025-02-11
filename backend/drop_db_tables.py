# backend/drop_db_tables.py
from sqlalchemy import create_engine, text
from app.models import Base
from app.config import DATABASE_URL

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Please define it in your environment.")

engine = create_engine(DATABASE_URL)

def drop_tables():
    with engine.connect() as conn:
        conn.execute(text("DROP SCHEMA public CASCADE;"))  # Drops all tables and constraints
        conn.execute(text("CREATE SCHEMA public;"))  # Recreates the schema
        print("All tables dropped successfully.")

if __name__ == "__main__":
    drop_tables()