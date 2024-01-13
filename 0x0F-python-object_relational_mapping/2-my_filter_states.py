#!/usr/bin/python3
"""
This module is about listing all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    try:
        # Connect to MySQL server
        db_connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object to execute queries
        cursor = db_connection.cursor()

        # Use format to create the SQL query with the user input
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

        # Execute the query
        cursor.execute(query)

        # Fetch and print the results
        results = cursor.fetchall()
        for result in results:
            print(result)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)

    finally:
        # Close the cursor and database connection
        cursor.close()
        db_connection.close()
