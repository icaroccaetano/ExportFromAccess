# Imports padrões
from datetime import datetime
from typing import TYPE_CHECKING

# Imports de terceiros
from sqlalchemy.orm import Mapped, mapped_column

# Imports locais
from app.config.db import db

class Concurso2022(db.Model):
    __tablename__ = 'SGDP_SISTEMA_CONCURSO_PROCESSOS'

    Nome_Canidato:              Mapped[str]
    CPF:                        Mapped[str]    
    DATA_POSSE:                 Mapped[datetime]    
    DATA_EFETIVO_EXERCICIO:     Mapped[datetime]
    PROCESSON:                  Mapped[str] 
    Cargo:                      Mapped[str]
    REGIAO:                     Mapped[str] 
    VINCULO:                    Mapped[str]