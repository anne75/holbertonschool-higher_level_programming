#!/usr/bin/python3
"""
This is module 102
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

    for c in session.query(City).order_by(City.id).all():
        print("{:d}: {:s} -> {:s}".format(c.id, c.name, c.state.name))

    session.commit()
    session.close()
    engine.dispose()
