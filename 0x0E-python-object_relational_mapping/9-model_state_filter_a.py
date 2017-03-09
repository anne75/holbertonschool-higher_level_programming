#!/usr/bin/python3
"""
This is module 9-model_state_filter_a
After using mysqldb to connect to a mysql database, same questions are done
again with sqlalchemy
"""
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), echo=False)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    for result in session.query(State.id, State.name).filter(
            State.name.like('%a%')).order_by(State.id):
        print("{:d}: {}".format(result[0], result[1]))

    session.close()
    engine.dispose()
