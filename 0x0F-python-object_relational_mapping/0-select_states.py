#!/usr/bin/python3
""" select state module """
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host="localhost", port=3306)
    cur = db.cursor()
    cur.execute("SELECT * from states")
    rows = cur.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
