#!/usr/bin/python3
"""
This is module 11-model_state_insert
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

    result = session.query(State).filter_by(id=2).first()
    result.name = "New Mexico"

    session.commit()   # otherwise not persistent
    session.close()
    engine.dispose()
