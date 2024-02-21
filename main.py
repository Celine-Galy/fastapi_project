from fastapi import FastAPI
from app.database.database import init_db
from app.routes.api import router


app = FastAPI()

@app.get('/')
async def root() -> str:
    init_db()
    return 'Hello, World!'

 
app.include_router(router)