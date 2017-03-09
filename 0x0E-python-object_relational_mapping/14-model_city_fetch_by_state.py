#!/usr/bin/python3
"""
This is module 14-model_fetch...
After using mysqldb to connect to a mysql database, same questions are done
again with sqlalchemy
"""
from model_state import Base, State
from model_city import City
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), echo=False)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    for res in session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id):
        print("{:s}: ({:d}) {:s}".format(res[0], res[1], res[2]))

    session.close()
    engine.dispose()
