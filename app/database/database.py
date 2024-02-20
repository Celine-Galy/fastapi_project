from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker


# Database configuration - PostgreSQL
# Think to create a .env file to store the sensitive data

db_user = 'postgres'
db_password = 'postgres'
db_host = 'localhost'
db_name = 'fastapi'
db_port = 5432

DATABASE_URL = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# Create the database engine
engine = create_engine(DATABASE_URL)

# Connect to the database
try:
    print('Connected to the database')
    # Create the tables
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
except Exception as e:
    print(f'Error: {e}')
    print('Failed to connect to the database')
    engine = None
    exit(1)