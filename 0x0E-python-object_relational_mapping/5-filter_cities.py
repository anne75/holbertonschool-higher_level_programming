#!/usr/bin/python3
"""
This is module 5-filter_cities
Again after module 4 a more advanced query
Could have used a JOIN and then restrict but I preferred to have 2 select
"""
import MySQLdb as mdb
import sys

if __name__ == "__main__":
    db = None
    if (len(sys.argv) != 5):
        print("Usage: ./0-select_states.py mysql_username "
              "mysql_password database_name state_name")
    else:
        db = mdb.connect(host="localhost",  port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

        c = db.cursor()
        command = """SELECT cities.name
        FROM cities
        WHERE cities.state_id IN
        (SELECT states.id
        FROM states
        WHERE states.name = %s);"""
        c.execute(command, (sys.argv[4],))
        print(", ".join(["{}".format(r[0]) for r in c.fetchall()]))

        c.close()
        db.close()
