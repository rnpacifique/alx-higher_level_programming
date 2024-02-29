#!/usr/bin/python3
"""
Script to print cities by states
"""

import MySQLdb
import sys


def main(username, password, database):
    """
    Function to handle the query execution
    """

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
            FROM cities INNER JOIN states ON cities.state_id = \
            states.id ORDER BY cities.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_states.py <username> \
                <password> <database>")
        sys.exit(1)
    username, password, database = sys.argv[1:]
    main(username, password, database)