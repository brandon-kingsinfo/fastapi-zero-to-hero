import db


def create_db():
    return db.Base.metadata.create_all(bind=db.engine)


def get_session():
    session = db.Session()

    try:
        yield session
    finally:
        session.close()

# create_db()
