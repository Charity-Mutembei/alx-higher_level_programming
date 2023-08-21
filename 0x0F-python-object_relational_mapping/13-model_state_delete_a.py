#!/usr/bin/python3
"""
This script deletes all State objects with a name containing the letter "a"
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

    # Create a connection to the MySQL server
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        mysql_username, mysql_password, database_name))

    # Bind the engine to the Base instance
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve State objects containing the letter "a"
    a_states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the State objects
    for state in a_states:
        session.delete(state)
    session.commit()


if __name__ == "__main__":
    main()
