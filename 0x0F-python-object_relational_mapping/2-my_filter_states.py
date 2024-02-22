#!/usr/bin/python3
"""
Script to list all  states with name that matching name given.
"""
import sys
import MySQLdb


def main(username, password, database, sname):
    """
    Function to select all states from database hbtn_0e_0_usa
    with name equal to name given as an argument.
    """

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)

    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name = '{}' \
                    ORDER BY id ASC".format(sname))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> \
                <password> <database> <sname>")
        sys.exit(1)

    username, password, database, sname = sys.argv[1:]
    main(username, password, database, sname)