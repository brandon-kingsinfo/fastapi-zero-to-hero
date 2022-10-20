import db


def create_db():
    return db.Base.metadata.create_all(bind=db.engine)


# create_db()
