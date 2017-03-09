#!/usr/bin/python3
"""
This is module model_state
This module defines one class definition: State
and an instance Base = declarative_base()
"""


from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sq

Base = declarative_base()


class City(Base):
    """
    Class City
    Linked to the MySQL table states

    **class attributes**
    id: auto-generated, unique integer, can't be null and is a primary key
    name: string with maximum 128 characters and can't be null
    state_id: integer, can't be null and is a foreign key to states.id
    """
    __tablename__ = "cities"
    id = sq.Column(sq.Integer, primary_key=True, nullable=False)
    name = sq.Column(sq.String(128), nullable=False)
    state_id = sq.Column(sq.Integer, sq.ForeignKey('states.id'),
                         nullable=False)

    def __str__(self):
        """fancy printing"""
        return "{}: {}".format(self.id, self.name)

    def __repr__(self):
        """print a class"""
        return "City(name={}, id={}), state_id={}".format(
            self.name, self.id, self.state_id)
