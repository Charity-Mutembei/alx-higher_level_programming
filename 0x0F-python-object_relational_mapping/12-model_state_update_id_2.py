#!/usr/bin/python3
"""
This script changes the name of a State object from the database hbtn_0e_6_usa.
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

    # Query the State object to update
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update the name of the State object
    if state_to_update is not None:
        state_to_update.name = "New Mexico"
        session.commit()
    else:
        print("State not found")


if __name__ == "__main__":
    main()
