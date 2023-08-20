#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv


def main():
    """Database credentials"""
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    """Connect to MySQL server"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username, passwd=mysql_password,
                         db=database_name)

    """Create a cursor to interact with the database"""
    cursor = db.cursor()

    """SQL query to retrieve cities sorted by id in ascending order"""
    query = "SELECT cities.id, cities.name, states.name FROM cities ORDER BY id ASC"

    """Execute the query"""
    cursor.execute(query)

    """Fetch all the results"""
    results = cursor.fetchall()

    """Display the results"""
    for row in results:
        print(row)

    """Close the cursor and database connection"""
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
