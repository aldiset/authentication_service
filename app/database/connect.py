from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set up the database connection
DATABASE_URL = "postgresql://user:password@localhost:5432/authdb"
engine = create_engine(DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)