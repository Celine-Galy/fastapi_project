from app.database.database import SessionLocal
from app.database.models import Commune
from fastapi import APIRouter

router = APIRouter()
communes = []

@router.get("/communes")
async def get_commune():
    session = SessionLocal()
    communes = session.query(Commune).all()
    return communes

@router.get("/commune/{nom_complet}")
async def get_commune_by_name(nom_complet: str):
    session = SessionLocal()
    commune = session.query(Commune).filter(Commune.nom_complet == nom_complet).first()
    return commune

@router.get("/communes/{code_departement}")
async def get_communes_by_department(code_departement: str) -> list:
    session = SessionLocal()
    communes_list = []
    communes = session.query(Commune).filter(Commune.code_departement == code_departement).all()
    for commune in communes:
        communes_list.routerend(commune.nom_complet)
    return communes_list

@router.post("/create")
async def create_commune(code_postal: str, nom_complet: str, code_departement: str):
    commune = Commune(code_postal=code_postal, nom_complet=nom_complet.upper(), code_departement=code_departement)
    session = SessionLocal()
    session.add(commune)
    session.commit()
    return {"commune created": commune}

@router.patch("/update")
async def update_commune(id:int ,code_postal: str, nom_complet: str, code_departement: str):
    session = SessionLocal()
    commune = session.query(Commune).filter(Commune.id == id).update({
            "code_postal": code_postal,
            "nom_complet": nom_complet, 
            "code_departement": code_departement
            })
    session.commit()
    return {"commune updated": commune}