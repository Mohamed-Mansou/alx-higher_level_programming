#!/usr/bin/python3
"""
Lists all values in the states tables of a database where name
matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE"
            " '{:s}' ORDER BY id ASC".format(argv[4]))
    cur = cursor.fetchall()
    for i in cur:
        if i[1] == argv[4]:
            print(i)
