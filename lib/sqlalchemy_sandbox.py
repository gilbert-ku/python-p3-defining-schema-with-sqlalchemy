# lib/sqlalchemy_sandbox.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

# Create a connection to the database
engine = create_engine('sqlite:///students.db')

# Create the table based on the defined model
Base.metadata.create_all(engine)

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata.create_all(engine)