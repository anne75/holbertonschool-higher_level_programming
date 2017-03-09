#!/usr/bin/python3
"""
This is module 13-model_state_delete
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

    result = session.query(State).filter(State.name.like('%a%')).all()
    session.delete(*result)

    session.commit() # otherwise not persistent
    session.close()
    engine.dispose()
