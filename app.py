from fastapi import FastAPI, Depends
import fastapi.security as security
import sqlalchemy.orm as orm
import schemas
import services
app = FastAPI()


@app.post("/api/v1/users")
async def register_user(user: schemas.UserRequest, session: orm.Session = Depends(services.get_session)):
    pass
