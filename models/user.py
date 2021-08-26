#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'
    places = relationship('Place', backref="user", cascade="all, delete")
    # class attribute places represents a relationship with the class Place
    # If the User object is deleted, all linked Place objects will be
    # automatically deleted. Also,the reference from a Place object to his
    # User is named user
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    reviews = relationship('Review', backref='user', cascade='all, delete')

    email = ""
    password = ""
    first_name = ""
    last_name = ""
