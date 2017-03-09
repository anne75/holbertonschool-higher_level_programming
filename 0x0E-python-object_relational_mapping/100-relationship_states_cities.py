#!/usr/bin/python3
"""
This is module 11-model_state_insert
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

    new_state = State(name="California")
    # print("state", new_state)
    new_city = City(name="San Francisco")
    # print("city", new_city.state)
    new_state.cities.append(new_city)
    # print("city", new_city.state)

    session.add(new_state)
    session.add(new_city)

    session.commit()
    session.close()
    engine.dispose()
