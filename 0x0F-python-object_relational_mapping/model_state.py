#!/usr/bin/python3
"""
Module for defining the State class and creating Base instance.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Create a Base instance
Base = declarative_base()

# Define the State class
class State(Base):
    """
    Represents a state in the hbtn_0e_4_usa database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
