# imports
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine

# create engine
engine = create_engine("sqlite:///data/database.db")

# base class for all database classes we need to use
class Base(DeclarativeBase):
    pass