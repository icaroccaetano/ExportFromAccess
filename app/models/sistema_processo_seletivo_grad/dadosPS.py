from sqlalchemy.orm import Mapped, mapped_column
from datetime import time

from app.config.db import db

class dados_servidores(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_SISTEMA_AUTOGED_DADOS_PS2022'

    # Define as colunas da tabela
    id:                         Mapped[int] = mapped_column(primary_key=True)
    nome:                       Mapped[str]
    cpf:                        Mapped[str]
    processo:                   Mapped[str]
    status:                     Mapped[str]
    admitido:                   Mapped[bool]