#!/usr/bin/python3
"""
This script lists all City objects from the database hbtn_0e_101_usa.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


def main():
    """Database credentials"""
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    # Create a connection to the MySQL server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        mysql_username, mysql_password, database_name))

    # Bind the engine to the Base instance
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve all City objects, sorted by id in ascending order
    cities = session.query(City).order_by(City.id).all()

    # Display the results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")


if __name__ == "__main__":
    main()
