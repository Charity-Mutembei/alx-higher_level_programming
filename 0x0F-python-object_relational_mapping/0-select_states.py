#!/usr/bin/python3
"""
This is a script that lists all states
from the database hbtn-0e_0_USA
"""


from sys import argv
import MySQLdb

"""
This is a script that lists all states
from the database hbtn-0e_0_USA
"""


def main():
    """Database credentials"""
    mysql_username = input("Enter MySQL username: ")
    mysql_password = input("Enter MySQL password: ")
    database_name = input("Enter database name: ")

    """Connect to MySQL server"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username, passwd=mysql_password,
                         db=database_name)

    """Create a cursor to interact with the database"""
    cursor = db.cursor()

    """SQL query to retrieve states sorted by id in ascending order"""
    query = "SELECT * FROM states"

    """Execute the query"""
    cursor.execute(query)

    """Fetch all the results"""
    results = cursor.fetchall()

    """Display the results"""
    for row in results:
        print(row)


if __name__ == "__main__":
    main()
