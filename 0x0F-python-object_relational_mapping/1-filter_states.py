#!/usr/bin/python3
"""
script that lists all states with a name
string N (upper N) from the database
hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv


"""
Below is a function of the above requirements
"""


def main():
    """takes the three arguments"""
    user = argv[1]
    password = argv[2]
    database = argv[3]

    """connect to the database"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password,
                         db=database)

    """Create a cursor to interact with the database"""
    cursor = db.cursor()

    """SQL query to retrieve states sorted by id in ascending order"""
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    """Execute the query"""
    cursor.execute(query)

    """Fetch all the results"""
    results = cursor.fetchall()

    """Display the results"""
    for row in results:
        print(row)


if __name__ == "__main__":
    main()
