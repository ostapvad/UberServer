from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from typing import Generator, List, Dict
from .config import POSTGRES_DB_URL

DATABASE_URL = POSTGRES_DB_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Credential(Base):
    __tablename__ = "credentials"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)


def get_db() -> Generator[Session, None, None]:
    """
    Returns DB generator
    :return:
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def query_credentials(db: Session, username: Credential.username, password: Credential.password) -> Dict:
    """
    Get credentials of user in DB
    :param db:
    :param username:
    :param password:
    :return:
    """
    data = db.query(Credential).filter(Credential.username == username, Credential.password == password).first()
    data = jsonable_encoder(obj=data)

    if not isinstance(data, dict):
        data = {}
    return data


def query_all(db: Session) -> List[Dict]:
    """
    Get the content of DB
    :param db:
    :return:
    """
    data = jsonable_encoder(obj=db.query(Credential).filter().all())
    if not data:
        data = []
    return data


print(query_credentials(db=next(get_db()), username="user2", password="222"))
print(query_all(db=next(get_db())))
