# app/database.py
import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL
"""
Database configuration module.

Creates a SQLAlchemy engine and session factory using DATABASE_URL.
Provides a dependency for obtaining a database session.
"""

# Configure logging for debugging database operations.
logging.basicConfig(level=logging.DEBUG)

# Create the SQLAlchemy engine with SQL statement echo enabled for debugging.
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured session factory.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Dependency function that provides a database session.

    Yields:
        db (Session): A SQLAlchemy session.
    """
    db = SessionLocal()
    logging.debug("Created a new database session")
    try:
        yield db
    finally:
        db.close()
        logging.debug("Closed the database session")

