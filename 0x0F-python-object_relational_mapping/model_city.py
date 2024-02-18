#!/usr/bin/python3
""" model state module """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from model_state import State, Base


class City(Base):
    """ state table class """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(ForeignKey('states.id'), nullable=False)
