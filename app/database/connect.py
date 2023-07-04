from pydantic import PostgresDsn
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Set up the database connection
DATABASE_URL = PostgresDsn.build(
    scheme="postgresql",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
    path="/authdb"
)
engine = create_engine(DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()