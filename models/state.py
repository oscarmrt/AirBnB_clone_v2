#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state')

    if getenv("HBNB_ENV") != 'db':
        @property
        def cities(self):
            '''Getter atribute for cities'''
            from models.city import City
            clist = []
            all_c = models.storage.all(City)
            for c in all_c.values():
                if c.state_id == self.id:
                    clist.append(c)
            return (clist)
