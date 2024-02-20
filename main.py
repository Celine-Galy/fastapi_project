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
            key3 = "département"
            value1 = '0' + row[2] if len(row[2]) == 4 else row[2]
            value2 = row[10].upper()
        # Take the first two characters of the value1 as value2 except if the length of value1 is 4 and 
        # if value begins with 97, take the first three characters
            value3 = value1[0:2] if value1[0:2] != "97" else value1[0:3]
            commune_dict = {key1: value1, key2: value2, key3: value3}
            result.append(commune_dict)

    return {"data": result}
