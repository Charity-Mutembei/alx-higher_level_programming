#!/usr/bin/python3
import MySQLdb
"""
This is a script that lists all states
from the database hbtn-0e_0_USA
"""


def main():
    # Database credentials
    mysql_username = input("Enter MySQL username: ")
    mysql_password = input("Enter MySQL password: ")
    database_name = input("Enter database name: ")

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username, passwd=mysql_password,
                         db=database_name)

    # Create a cursor to interact with the database
    cursor = db.cursor()

    # SQL query to retrieve states sorted by id in ascending order
    query = "SELECT * FROM states ORDER BY id ASC"

    try:
        # Execute the query
        cursor.execute(query)

        # Fetch all the results
        results = cursor.fetchall()

        # Display the results
        print("States:")
        for row in results:
            state_id, state_name = row
            print(f"{state_id}: {state_name}")

    except MySQLdb.Error as e:
        print("Error:", e)

    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()


if __name__ == "__main__":
    main()
