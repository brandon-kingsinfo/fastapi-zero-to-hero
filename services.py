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
'''description of getUserByEmail'''


async def getUserByEmail(email: str, session: _orm.Session):
    rs = session.query(_models.UserModel).filter(
        _models.UserModel.email == email).first()

    if rs:
        return {"status": True, "data": rs}

    return {"status": False, "errmsg": f"email {email} not found"}
