from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class Commune(Base):
    __tablename__ = 'communes'

    id = Column(Integer, primary_key=True, index=True)
    nom_complet = Column(String)
    code_postal = Column(String)
    code_departement = Column(String)

    def __repr__(self):
        return f"Commune(id={self.id}, nom_complet={self.nom_complet}, code_postal={self.code_postal}, code_departement={self.code_departement})"

