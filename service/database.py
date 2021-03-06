from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./service.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Session = sessionmaker(engine)

Base = declarative_base()
