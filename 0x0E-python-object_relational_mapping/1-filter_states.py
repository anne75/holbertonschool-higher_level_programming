#!/usr/bin/python3
"""
This is module 1-filter_states
It builds on the last module to query only some state names
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
        c.execute("""SELECT *
        FROM states
        WHERE NAME LIKE BINARY 'N%' ORDER BY id ASC;""")
        for r in c.fetchall():
            print(r)

        c.close()
        db.close()
