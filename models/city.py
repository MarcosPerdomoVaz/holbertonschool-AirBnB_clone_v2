#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.state import State


class City(BaseModel):
    """ The city class, contains state ID and name """
    if models.is_type == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey(State.id), nullable=False)
        place = relationship('Place', backref='ciries', cascade='delate')
    else:
        state_id = ""
        name = ""
