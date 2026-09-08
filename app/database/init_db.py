from app.database.connection import Base, engine
from app.database.models import UserDB, PasswordEntryDB

def create_database():
    Base.metadata.create_all(engine)

create_database()

