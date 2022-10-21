import db as _db
import models as _models
import sqlalchemy.orm as _orm


def create_db():
    return _db.Base.metadata.create_all(bind=_db.engine)


def get_session():
    session = _db.Session()

    try:
        yield session
    finally:
        session.close()


# create_db()
async def getUserByEmail(email: str, session: _orm.Session):
    return session.query(_models.UserModel).filter(
        _models.UserModel.email == email).first()
