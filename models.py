from datetime import datetime
import sqlalchemy
import sqlalchemy.orm as orm
import passlib.hash as hash
import db as db


class UserModel(db.Base):
    __tablename__ = "users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    phone = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    password_hash = sqlalchemy.Column(sqlalchemy.String)
    created_at = sqlalchemy.Column(
        sqlalchemy.DateTime, default=datetime.utcnow)
