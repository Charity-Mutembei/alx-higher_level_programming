#!/usr/bin/python3
"""
This script lists all State objects and corresponding City objects
contained in the database hbtn_0e_101_usa.
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

    """
    # Query to retrieve State objects along
    # with their corresponding City objects
    """
    states_with_cities = session.query(State).order_by(
        State.id).all()

    # Display the results
    for state in states_with_cities:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")


if __name__ == "__main__":
    main()
