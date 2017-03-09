#!/usr/bin/python3
"""
This is module 101
After using mysqldb to connect to a mysql database, same questions are done
again with sqlalchemy
"""
from relationship_state import Base, State
from relationship_city import City
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), echo=False)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id).all()
    for s in states:
        print("{:d}: {:s}".format(s.id, s.name))
        for c in sorted(s.cities, key=lambda x: x.id):
            print("    {:d}: {:s}".format(c.id, c.name))

    session.commit()
    session.close()
    engine.dispose()
