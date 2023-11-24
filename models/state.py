#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances
        with state_id equals to the current State.id"""
        from models.city import City
        from models import storage
        list_cities = []
        for city in storage.all(City).values():
            if self.id == city.state_id:
                list_cities.append(city)
        return list_cities
