#!/usr/bin/python3
"""
Script taking in four arguments
"""


from sys import argv
import MySQLdb


def main():
    """Database credentials"""
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    """Connect to the database"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=database)

    """Create a cursor to interact with the database"""
    cursor = db.cursor()

    """
    SQL query to retrieve states with
    names matching the argument,
    sorted by id in ascending order
    """
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

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
