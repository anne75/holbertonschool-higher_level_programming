#!/usr/bin/python3
"""
This is module 3-my_safe_filter_states
In this module, we do that same thing as un module 2, but using mysqldb
to pass a parameter in a SQL query.
This way we use mysqldb parametrization tool to avoid code injection
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
        command = "SELECT * FROM states WHERE name = '{:s}' ORDER BY id ASC;"
        c.execute("SELECT * FROM states WHERE "
                  "name = '{:s}' ORDER BY id ASC;".format(sys.argv[4],))
        for r in c.fetchall():
            print(r)

        c.close()
        db.close()
