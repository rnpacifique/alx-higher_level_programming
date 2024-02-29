#!/usr/bin/python3
"""
Script to list cities of the state given as argument.
"""

import sys
import MySQLdb


def main(username, password, database, state):
    """
    Function to implement so.
    """

    try:
        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                passwd=password,
                db='hbtn_0e_4_usa'
                )

        cursor = db.cursor()
        cursor.execute("SELECT name FROM cities WHERE \
                state_id = (SELECT id FROM state\
                WHERE name = %s) \
                ORDER BY cities.id ASC", (state))

        rows = cursor.fetchall()
        city_names = [row[0] for row in rows]
        print(', '.join(city_names))

        print()

    except MySQLdb.Error as e:
        print("MySQLdb Error: {}".format(e))

    finally:
        if db:
            db.close()
        if cursor:
            cursor.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Remember the Usage?")
        sys.exit(1)

    username, password, database, state = sys.argv[1:]
    main(username, password, database, state)