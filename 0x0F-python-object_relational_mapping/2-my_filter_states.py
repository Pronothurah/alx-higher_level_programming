#!/usr/bin/python3
"""
This module is about listing all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv[1:]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[0],
        password=args[1],
        database=args[2]
    )
    cur = db.cursor()
    query = """
    SELECT * FROM states
    WHERE BINARY `name`='{query}'
    ORDER BY id ASC
    """
    cur.execute(query.format(query=args[3]))
    for data in cur.fetchall():
        print(data)
    cur.close()
    db.close()
