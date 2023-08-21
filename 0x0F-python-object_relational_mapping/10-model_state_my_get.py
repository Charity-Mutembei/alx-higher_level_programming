#!/usr/bin/python3
"""
This script prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def main():
    """Database credentials"""
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    search_name = argv[4]

    # Create a connection to the MySQL server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        mysql_username, mysql_password, database_name))

    # Bind the engine to the Base instance
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve the State object with the specified name
    state = session.query(State).filter(
        State.name == search_name).first()

    # Display the result
    if state is not None:
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    main()
