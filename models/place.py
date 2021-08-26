#!/usr/bin/python3
""" Place Module for HBNB project """

from sqlalchemy import Table
from sqlalchemy.orm import backref, relationship
from models.base_model import BaseModel
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Float, Integer, String
from models.base_model import Base, BaseModel


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', backref='place',
                           cascade=('all, delete'))
    metadata = Base.metadata
    place_amenity = Table('place_amenity', metadata,
                          Column('place_id', String(60), ForeignKey(
                                'places.id'), primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60), ForeignKey(
                                'amenities.id'), primary_key=True,
                                nullable=False))
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    @property
    def reviews(self):
        """
        returns the list of Review instances with place_id equals to the
        current Place.id
        """
        from models.review import Review
        from models import storage
        reviews_list = []
        for rev in storage.all(Review).values():
            if rev.place_id == self.id:
                reviews_list.append(rev)
        return reviews_list

    @property
    def amenities(self):
        from models.amenity import Amenity
        import models
        amenity_list = []
        for amn_descr in models.storage.all(Amenity).values():
            if amn_descr.id == self.id:
                amenity_list.append(amn_descr)
        return amenity_list

    @amenities.setter
    def amenities(self, obj):
        if type(obj) == "Amenity":
            self.amenities_id.append(obj)
