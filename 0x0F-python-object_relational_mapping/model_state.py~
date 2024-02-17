#!/usr/bin/python3
""" model state module """
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base  = declarative_base()
class State(Base):
    """ state table class """
    __tablename__  = "states"
    id = Column(Integer, nullable=False, primary_key=True,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)

