import csv
from sqlalchemy import create_engine, text
from app.database.models import  Commune, Base
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
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
def read_csv():
    with open('communes-departement-region.csv', newline='', encoding='utf-8') as csvfile:
        data = list(csv.reader(csvfile))
        result = []
        for row in data[1:]:
        # Take entries of the first row as keys
            code_postal = data[0][2]
            nom_complet = data[0][10]
            code_departement = "département"
        # Take the entries of the current row as values
            if len(row[2]) == 4:
                code_postal_value = '0' + row[2]
            else:
                code_postal_value = row[2]
           
            nom_complet_value = row[10].upper()
        # Take the first two characters of the value1 as value2 except if the length of value1 is 4 and 
        # if value begins with 97,98,99 take the first three characters
            if code_postal_value[0:2] == "97" or code_postal_value[0:2] == "98" or code_postal_value[0:2] == "99":
                code_departement_value = code_postal_value[0:3]
            else:
                code_departement_value = code_postal_value[0:2]
            commune_dict = {code_postal: code_postal_value, nom_complet: nom_complet_value, code_departement: code_departement_value}
            result.append(commune_dict)
            populate_db(commune_dict)
    print('Data inserted successfully', result[0:5])
    return result

def populate_db(commune_dict):
    commune = commune_dict = Commune(code_postal=commune_dict['code_postal'], nom_complet=commune_dict['nom_commune_complet'], code_departement=commune_dict['département'])
    try:
        session.add(commune)
        
    except Exception as e:
        print(f'Error: {e}')
        print('Rolling back the session')
        raise e

def create_db():
    try:
        session.execute(text(f"CREATE DATABASE {db_name}"))
       
        print('Database created successfully')
    except Exception as e:
        print(f'Error: {e}')
        raise e
    finally:
        print('Database creation completed')

def bd_is_created():
    try:
        check_db = session.execute(text(f"SELECT 1 FROM pg_database WHERE datname='{db_name}'"))
        if check_db.rowcount == 1:
            print('Database exists')
            return True
        else:
            print('Database does not exist')
            return False
    except Exception as e:
        print(f'Error: {e}')
        raise e
    finally:
        print('Database check completed')

def init_db():
    Base.metadata.drop_all(bind=engine)
    # Check if the database exists
    if bd_is_created() == False:
        try:
            create_db()
            Base.metadata.create_all(bind=engine)
            read_csv()
        except Exception as e:
            print(f'Error: {e}')
            raise e
        finally:
            print('Database initialization completed')
    else:
        print('Database already exists')
        Base.metadata.create_all(bind=engine)
        read_csv()
        print('Database initialization completed')
    session.commit()
    session.close()

