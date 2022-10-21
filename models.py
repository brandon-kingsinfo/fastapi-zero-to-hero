from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
import sqlalchemy.orm as _orm
import passlib.hash as _hash
import db as _db


class UserModel(_db.Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    created_at = Column(
        DateTime, default=datetime.utcnow())
    posts = _orm.relation("PostModel", back_populates="user")

    def password_verification(self, password: str):
        return _hash.bcrypt.verify(password, self.password_hash)


class PostModel(_db.Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_title = Column(String, index=True)
    post_description = Column(String)
    image = Column(String)
    created_at = Column(
        DateTime, default=datetime.utcnow())
    user = _orm.relation("UserModel", back_populates="posts")
