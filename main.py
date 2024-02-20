from fastapi import FastAPI
import csv


app = FastAPI()


@app.get('/')
async def root() -> str:
    return 'Hello, World!'

@app.get('/communes')
async def communes() -> dict:
    return read_csv()
    

def read_csv():
    with open('communes-departement-region.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))
        result = []
        for row in data[1:]:
        # Take two  entries of the first row as keys
            key1 = data[0][2]
            key2 = data[0][10]
            value1 = row[2]
            value2 = row[10]
            commune_dict = {key1: value1, key2: value2}
            result.append(commune_dict)

   
    return {"data": result[0:10]}
