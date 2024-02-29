#!/usr/bin/python3
"""
The module to use SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    This is the definition of the State class.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    db_engine = create_engine('mysql://your_username:your_password@localhost:3306/your_database')

    Base.metadata.create_all(db_engine)
