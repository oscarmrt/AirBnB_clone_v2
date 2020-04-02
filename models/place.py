#!/usr/bin/python3
"""This is the place class"""
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, Float, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


if models.storage_t == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', onupdate='CASCADE',
                                 ondelete='CASCADE'), nullable=False,
                                 primary_key=True)
                          Colunm('amenity_id', Stirng(60),
                                 ForeignKey('amenities.id', onupdate='CASCADE',
                                 ondelete='CASCADE'),
                                 nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    if models.storage_t == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities", viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if models.storage_t != 'db':
        @property
        def review_method(self):
            '''Getter atribute for review'''
            from models.review import Review
            rlist = []
            all_r = models.storage.all(Review)
            for r in all_r.values():
                if r.place_id == self.id:
                    rlist.append(r)
            return (rlist)

        @property
        def amenity_method(self):
            '''Getter atribute for amenity'''
            from models.amenity import Amenity
            alist = []
            all_a = models.storage.all(Amenity)
            for a in all_a.values():
                if a.place_id == self.id:
                    alist.append(a)
            return (alist)
