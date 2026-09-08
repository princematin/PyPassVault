# imports
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.database.connection import Base
from datetime import datetime
from sqlalchemy import JSON

# user database class with SQLalchemy
class UserDB(Base):
    __tablename__ = "users"


    id : Mapped[int] = mapped_column(primary_key= True)
    first_name : Mapped[str]
    last_name : Mapped[str]
    username : Mapped[str] = mapped_column(nullable= False)
    email : Mapped[str] = mapped_column(nullable= False)
    password_hash : Mapped[str]
    created_at : Mapped[datetime] = mapped_column(default= datetime.now)
    updated_at : Mapped[datetime] = mapped_column(default= datetime.now,onupdate= datetime.now)

# passwordentry class with SQLalchemy
class PasswordEntryDB(Base):
    __tablename__ = "entries"

    id : Mapped[int] = mapped_column(primary_key= True)
    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"))
    site_name : Mapped[str]
    username : Mapped[str]
    password : Mapped[str]
    url : Mapped[str]
    tags : Mapped[list[str]] = mapped_column(JSON)
    created_at : Mapped[datetime] = mapped_column(default= datetime.now)
    updated_at : Mapped[datetime] = mapped_column(default= datetime.now, onupdate= datetime.now)
