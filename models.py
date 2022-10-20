from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
import sqlalchemy.orm as orm
import passlib.hash as hash
import db as db


class UserModel(db.Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    created_at = Column(
        DateTime, default=datetime.utcnow)


class PostModel(db.Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_title = Column(String, index=True)
    post_description = Column(String)
    created_at = Column(
        DateTime, default=datetime.utcnow)
