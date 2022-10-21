from fastapi import FastAPI, Depends, HTTPException
import fastapi.security as _security
import sqlalchemy.orm as _orm
import schemas as _schemas
import services as _services

app = FastAPI()


@app.post("/api/v1/users")
async def register_user(user: _schemas.UserRequest, session: _orm.Session = Depends(_services.get_session)):
    '''if email exists return error'''
    user = await _services.getUserByEmail(user.email, session)

    if user:
        raise HTTPException(status_code=400, detail="email already exists")
