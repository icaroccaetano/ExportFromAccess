# =================================================================================================================================================================
# Imports
# =================================================================================================================================================================

# Imports padrões
from datetime import datetime
from typing import TYPE_CHECKING, List

# Imports de terceiros
from sqlalchemy.orm import Mapped, mapped_column

# Imports locais
from app.config.db import db

# =================================================================================================================================================================
# Type para o mapping de colunas
# =================================================================================================================================================================

if TYPE_CHECKING:
    from app.models.base.RubricaVinculo import RubricaVinculo

# =================================================================================================================================================================
# Model de Referencia
# =================================================================================================================================================================

class Referencia(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_REFERENCIAS'

    # Define as colunas da tabela
    id:                         Mapped[int] = mapped_column(primary_key=True)
    mes:                        Mapped[str]
    ano:                        Mapped[int]
    comparativos_de_diferencas: Mapped[str]
    comparativos:               Mapped[str]
    bloqueios:                  Mapped[str]
    entrega_tesouro:            Mapped[str]
    atualizado_em:              Mapped[datetime]
    criado_em:                  Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    rubricas_vinculos: Mapped[List["RubricaVinculo"]] = db.relationship("RubricaVinculo", back_populates='referencia')