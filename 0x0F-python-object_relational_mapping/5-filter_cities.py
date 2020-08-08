#!/usr/bin/python3
""" Script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = db.cursor()
    state = sys.argv[4]
    i = 1

    num = cur.execute("SELECT cities.name FROM cities WHERE state_id = ( \
        SELECT id FROM states WHERE name LIKE BINARY %s) \
        ORDER BY cities.id", (state, ))
    res = cur.fetchall()
    for row in res:
        print(row[0], end="")
        if i < num:
            print(end=", ")
            i += 1
    print()
    cur.close()
    db.close()
