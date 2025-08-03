from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine

from app.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
