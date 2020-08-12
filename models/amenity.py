#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class Amenity(BaseModel, Base):
    """Amenities of places"""
    __tablename__ = "amenities"
    #name = Column(String(128), nullable=False)
