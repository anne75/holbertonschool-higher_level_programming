#!/usr/bin/python3
"""
This is module 4-cities_by_state
Building on the previous questions, we make a more advanced query with JOIN
"""
import MySQLdb as mdb
import sys

if __name__ == "__main__":
    db = None
    if (len(sys.argv) != 4):
        print("Usage: ./0-select_states.py mysql_username "
              "mysql_password database_name")
    else:
        db = mdb.connect(host="localhost",  port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

        c = db.cursor()
        command = """SELECT cities.id, cities.name, states.name
        FROM states
        INNER JOIN cities ON states.id = cities.state_id
        ORDER BY cities.id ASC;"""
        c.execute(command)
        for r in c.fetchall():
            print(r)

        c.close()
        db.close()
