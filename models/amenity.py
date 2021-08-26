#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy import Table
from sqlalchemy.sql.schema import ForeignKey


class Amenity(BaseModel, Base):
    """
    Details the place amenities
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
