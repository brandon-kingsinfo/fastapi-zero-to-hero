import fastapi as _fastapi
import fastapi.security as _security
import sqlalchemy.orm as _orm
import schemas as _schemas
import services as _services
import os

print(os.getenv("JWT_SECRET"))
app = _fastapi.FastAPI()


@app.post("/api/v1/users")
async def register_user(user: _schemas.UserRequest, session: _orm.Session = _fastapi.Depends(_services.get_session)):
    '''if email exists return error'''
    existing_user = await _services.getUserByEmail(user.email, session)

    if existing_user:
        raise _fastapi.HTTPException(
            status_code=400, detail="email already exists")

    # create the user and return a token

    new_user = await _services.create_user(user, session)

    return await _services.create_token(new_user)


@app.post("/api/v1/login")
async def login(formdata: _security.OAuth2PasswordRequestForm = _fastapi.Depends(),
                session: _orm.Session = _fastapi.Depends(_services.get_session)):
    user = await _services.login(formdata.username, formdata.password, session)

    if not user:
        raise _fastapi.HTTPException(
            status_code=401, detail="wrong login credentials")

    return await _services.create_token(user)


@app.get("/api/v1/current-user", response_model=_schemas.UserResponse)
async def current_user(user: _schemas.UserResponse = _fastapi.Depends(_services.current_user)):
    return user
