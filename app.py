from fastapi import FastAPI, Depends
import fastapi.security as _security
import sqlalchemy.orm as _orm
import schemas as _schemas
import services as _services

app = FastAPI()


@app.post("/api/v1/users")
async def register_user(user: _schemas.UserRequest, session: _orm.Session = Depends(_services.get_session)):
    pass
