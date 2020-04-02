#!/usr/bin/python3
"""This is the amenity class"""
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""
