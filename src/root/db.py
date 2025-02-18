""" Module contains db objects. """

import typing as t
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session

from root.app import app
from root.settings import DATABASE_URL, DEBUG


app.config.update({
    'SQLALCHEMY_DATABASE_URI': DATABASE_URL,
    'SQLALCHEMY_ECHO': DEBUG,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
})
db = SQLAlchemy(app)

BaseModel = db.Model
session = db.session


@contextmanager
def connection() -> t.Iterator[Session]:
    """ Context manager for creation of separate db session. """
    new_session = db.create_scoped_session()
    try:
        yield new_session
        new_session.commit()
    except Exception:
        new_session.rollback()
        raise
    finally:
        new_session.close()


@contextmanager
def transaction() -> t.Iterator[Session]:
    """ Context manager for markup of transactions. """
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
