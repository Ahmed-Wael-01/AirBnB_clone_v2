#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
    if models.storage_t != "db":
        @property
        def cities(self):
            """gets all cities linked to state"""
            linked_city = []
            cities = model.storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    linked_city.append(city)
            return linked_city
