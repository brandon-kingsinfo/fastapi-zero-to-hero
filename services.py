import db as _db
import models as _models
import sqlalchemy.orm as _orm
import schemas as _schemas
import email_validator as _email_validator
import fastapi as _fastapi
import passlib.hash as _hash
import jwt as _jwt
import os as _os


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


async def create_user(user: _schemas.UserRequest, session: _orm.Session):
    try:
        isValid = _email_validator.validate_email(user.email)
        email = isValid.email
    except _email_validator.EmailNotValidError:
        raise _fastapi.HTTPException(
            status_code=400, detail="invalid email fromat")

    hashed_password = _hash.bcrypt(user.password)

    user_obj = _models.UserModel(
        email=email,
        name=user.name,
        phone=user.phone,
        password_hash=hashed_password
    )

    session.add(user_obj)
    session.commit()

    # refresh user_obj with committed data
    session.refresh(user_obj)

    return user_obj


async def create_token(user: _models.UserModel):
    # convert user model to user schema
    user_schema = _schemas.UserBase.from_orm(user)

    # convert a pydantic object to dictionary
    user_dict = user_schema.dict()

    # remove the "created_at" key, so we don't break the token
    del user_dict["created_at"]

    token = _jwt.encode(user_dict, _os.getenv("JWT_TOKEN"))

    return dict(access_token=token, token_type="bearer")
