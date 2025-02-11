# app/models/base.py
"""
Base module for SQLAlchemy models.

Defines the declarative base class that all models will inherit from.
"""

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
