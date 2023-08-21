#!/usr/bin/python3
"""
Module for defining the State class.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


# Define the State class
class State(Base):
    """
    Represents a state in the hbtn_0e_100_usa database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
