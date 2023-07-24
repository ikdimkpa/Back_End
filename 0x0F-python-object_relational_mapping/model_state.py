#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

# The following code should be placed after the class definition and the necessary imports
# It establishes a connection to the MySQL server and creates the tables defined by the classes
from sqlalchemy import create_engine

# Replace the placeholders with your MySQL credentials and database name
username = '<mysql_username>'
password = '<mysql_password>'
database = '<database_name>'

engine = create_engine("".format('mysql://{username}:{password}@localhost:3306/{database}'))
Base.metadata.create_all(engine)
