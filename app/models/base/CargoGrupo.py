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
    from app.models.base.Cargo import Cargo

# =================================================================================================================================================================
# Model de CargoGrupo
# =================================================================================================================================================================

class CargoGrupo(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_CARGOS_GRUPOS'

    # Define as colunas da tabela
    id:                             Mapped[int] = mapped_column(primary_key=True)
    descricao:                      Mapped[str]
    tipo:                           Mapped[str]
    categoria_trabalhador:          Mapped[str]
    unidade_de_pagamento:           Mapped[str]
    tipo_de_contrato_de_trabalho:   Mapped[str]
    regime_previdencia:             Mapped[str]
    status:                         Mapped[str]
    atualizado_em:                  Mapped[datetime]
    criado_em:                      Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    cargos:                         Mapped[List["Cargo"]] = db.relationship("Cargo", back_populates='cargo_grupo')