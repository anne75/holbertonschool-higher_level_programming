#!/usr/bin/python3
"""
This is module 2-my_filter_states
This modules builds on the previous one, selecting rows matching a value given
in a parameter.
We were required to use str.format() to see what SQL injection is
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
        command = """SELECT *
        FROM states
        WHERE name = '{0}' ORDER BY id ASC;""".format(sys.argv[4])
        c.execute(command)
        for r in c.fetchall():
            print(r)

        c.close()
        db.close()

# Single quotes around {0} are necessary
