import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.models import Base, Commune

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
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def read_csv():
    with open('communes-departement-region.csv', newline='', encoding='utf-8') as csvfile:
        data = list(csv.reader(csvfile))
        result = []
        for row in data[1:]:
        # Take two  entries of the first row as keys
            code_postal = data[0][2]
            nom_complet = data[0][10]
            code_departement = "département"
            value1 = row[2] if len(row[2]) != 4 else '0' + row[2]
            value2 = row[10].upper()
        # Take the first two characters of the value1 as value2 except if the length of value1 is 4 and 
        # if value begins with 97,98,99 take the first three characters
            value3 = value1[0:3] if value1[0:2] == "97" or value1[0:2] == "98" or value1[0:2] == "99" else value1[0:2]
            commune_dict = {code_postal: value1, nom_complet: value2, code_departement: value3}
            result.append(commune_dict)
            populate_db(commune_dict)
    return result

def populate_db(commune_dict):
    commune = commune_dict = Commune(code_postal=commune_dict['code_postal'], nom_complet=commune_dict['nom_commune_complet'], code_departement=commune_dict['département'])
    session = SessionLocal()
    session.add(commune)
    session.commit()
    session.refresh(commune)
    session.close()


def init_db():
    try:
        print('Connected to the database')
        # Create the tables
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        db = SessionLocal()
        read_csv()
        db.close()
        
    except Exception as e:
        print(f'Error: {e}')
        print('Failed to connect to the database')

    finally:
        print('Database connection closed')
        db.close()