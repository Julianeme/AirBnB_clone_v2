#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    name = ""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state", cascade="all, delete")
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """
            returns the list of City
            instances with state_id equals to the current State.id
            """
            from models import storage
            from models.city import City
            cities_list = []
            for cities in storage.all(City).values():
                if cities.state_id == self.id:
                    cities_list.append(cities)
            return cities_list
