#!/usr/bin/python3
"""
This script takes the name of a state as an argument
and lists all cities of that state from the database hbtn_0e_4_usa.
"""


import MySQLdb
from sys import argv


def main():
    """Database credentials"""
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    """Connect to MySQL server"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username, passwd=mysql_password,
                         db=database_name)

    """Create a cursor to interact with the database"""
    cursor = db.cursor()

    """SQL query to retrieve cities of the
    specified state, sorted by id in ascending order"""
    query = """
        SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE BINARY %s
        ORDER BY cities.id ASC
    """

    """Execute the query with the provided state name"""
    cursor.execute(query, (state_name,))

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
