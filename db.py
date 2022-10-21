import sqlalchemy as _sqlalchemy
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DB_URL = "sqlite:///./dbfile.db"
engine = _sqlalchemy.create_engine(
    DB_URL, connect_args={"check_same_thread": False})
Session = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
