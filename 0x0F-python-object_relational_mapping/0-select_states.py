#!/usr/bin/python3
"""Script that lists all states from a database"""
import sys
import MySQLdb


if __name__ == "__main__":
    if len(sys.argv) >= 4:
        db_connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        for data in cursor.fetchall():
            if (str(data[1]).startswith('N')):
                print(data)
        db_connection.close()
