# =================================================================================================================================================================
# Imports
# =================================================================================================================================================================

# Imports padrões
from datetime import datetime, date
from typing import TYPE_CHECKING, List

# Imports de terceiros
from sqlalchemy.orm import Mapped, mapped_column

# Imports locais
from app.config.db import db

# =================================================================================================================================================================
# Type para o mapping de colunas
# =================================================================================================================================================================

if TYPE_CHECKING:
    from app.models.base.RubricaGrupo import RubricaGrupo
    from app.models.base.RubricaVinculo import RubricaVinculo

# =================================================================================================================================================================
# Model de Rubrica
# =================================================================================================================================================================

class Rubrica(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_RUBRICAS'

    # Define as colunas da tabela
    id:                 Mapped[int] = mapped_column(primary_key=True)
    grupo_rubricas_id:  Mapped[int] = mapped_column(db.ForeignKey('SGDP_RUBRICAS_GRUPOS.id'))
    nome_abreviado:     Mapped[str]
    classe:             Mapped[str]
    tipo:               Mapped[str]
    data_inclusao:      Mapped[date]
    status:             Mapped[str]
    atualizado_em:      Mapped[datetime]
    criado_em:          Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    grupo_rubrica:                Mapped["RubricaGrupo"] = db.relationship("RubricaGrupo", back_populates='rubricas')
    rubricas_vinculos: Mapped[List["RubricaVinculo"]] = db.relationship("RubricaVinculo", back_populates='rubrica')