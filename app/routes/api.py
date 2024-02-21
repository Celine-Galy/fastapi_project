from app.database.database import SessionLocal
from sqlalchemy import func
from app.database.models import Commune
from fastapi import APIRouter

router = APIRouter()
communes = []
session = SessionLocal()

@router.get("/communes")
async def get_commune():
    communes = session.query(Commune).all()
    return communes

@router.get("/commune/{nom_complet}")
async def get_commune_by_name(nom_complet: str):
    commune = session.query(Commune).filter(func.lower(Commune.nom_complet) == func.lower(nom_complet)).all()
    return commune

@router.get("/communes/{code_departement}")
async def get_communes_by_department(code_departement: str) -> list:
    communes_list = []
    communes = session.query(Commune).filter(Commune.code_departement == code_departement).all()
    for commune in communes:
        communes_list.append(commune.nom_complet)
    return communes_list

@router.post("/create")
async def create_commune(code_postal: str, nom_complet: str, code_departement: str):
    commune = Commune(code_postal=code_postal, nom_complet=nom_complet.upper(), code_departement=code_departement)
    session.add(commune)
    session.commit()
    return {"commune created": commune}

@router.patch("/update")
async def update_commune(id:int ,code_postal: str, nom_complet: str, code_departement: str):
    commune = session.query(Commune).filter(Commune.id == id).update({
            "code_postal": code_postal,
            "nom_complet": nom_complet, 
            "code_departement": code_departement
            })
    session.commit()
    return {"commune updated": commune}

session.close()