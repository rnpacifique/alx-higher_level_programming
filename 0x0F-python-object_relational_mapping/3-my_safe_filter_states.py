#!/usr/bin/python3
"""
Script to display all states matching name
without worrying about the SQL Injection.
"""

import sys
import MySQLdb


def main(username, password, database, sname):
    """
    Function that handles the SQL Injection.
    """

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE \
            name = %s ORDER BY id", (sname, ))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
                "Usage: ./my_safe_filter_states.py\
                        <username> <password> <database>")
        sys.exit(1)

    username, password, database, sname = sys.argv[1:]

    main(username, password, database, sname)