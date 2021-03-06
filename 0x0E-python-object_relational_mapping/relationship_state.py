#!/usr/bin/python3
"""
This is module model_state
This module defines one class definition: State
and an instance Base = declarative_base()
"""


from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sq

Base = declarative_base()


class State(Base):
    """
    Class State
    Linked to the MySQL table states

    **class attributes**
    id: auto-generated, unique integer, can't be null and is a primary key
    name: string with maximum 128 characters and can't be null
    cities: a relationship with class City, on cascade delete
    """
    __tablename__ = "states"
    id = sq.Column(sq.Integer, primary_key=True, nullable=False)
    name = sq.Column(sq.String(128), nullable=False)

    cities = sq.orm.relationship("City", backref="state",
                                 cascade="all, delete, delete-orphan")

    def __str__(self):
        """fancy printing"""
        return "{}: {}".format(self.id, self.name)

    def __repr__(self):
        """print a class"""
        return "State(name={}, id={})".format(self.name, self.id)

# Also, the reference from a City object to his State should be named state
# what does it mean without touching the City class
