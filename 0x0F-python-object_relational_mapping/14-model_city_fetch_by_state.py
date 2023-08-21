#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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

    # Query to retrieve City objects along with their state names
    cities = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()

    # Display the results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")


if __name__ == "__main__":
    main()
