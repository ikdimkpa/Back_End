#!/usr/bin/python3
"""Module to connect to MySQL Database and run a query"""
import MySQLdb
import sys

if __name__ == '__main__':
    connect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           password=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = connect.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    connect.close()
