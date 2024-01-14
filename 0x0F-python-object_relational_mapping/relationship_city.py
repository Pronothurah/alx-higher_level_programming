#!/usr/bin/python3
"""
This module contains the class definition of a City and
an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    City ORM definition

    Attributes:
        - __tablename__ => the name of the table
        - id => the ID of the table columns
        - name => the name of the table columns
        - state_id => foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
