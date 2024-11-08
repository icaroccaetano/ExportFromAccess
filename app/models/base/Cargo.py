# =================================================================================================================================================================
# Imports
# =================================================================================================================================================================

# Imports padrões
from datetime import date, datetime
from typing import TYPE_CHECKING, List

# Imports de terceiros
from sqlalchemy.orm import Mapped, mapped_column

# Imports locais
from app.config.db import db

# =================================================================================================================================================================
# Type para o mapping de colunas
# =================================================================================================================================================================

if TYPE_CHECKING:
    from app.models.base.CargoGrupo import CargoGrupo
    from app.models.base.Vinculo import Vinculo

# =================================================================================================================================================================
# Model de Cargo
# =================================================================================================================================================================

class Cargo(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_CARGOS'

    # Define as colunas da tabela
    id:                     Mapped[int] = mapped_column(primary_key=True)
    descricao:              Mapped[str]
    cargos_grupos_id:       Mapped[int] = mapped_column(db.ForeignKey('SGDP_CARGOS_GRUPOS.id'))
    estrutura_salarial:     Mapped[str]
    jornada_de_trabalho:    Mapped[str]
    simbolo:                Mapped[str]
    data_de_extincao:       Mapped[date]
    atualizado_em:          Mapped[datetime]
    criado_em:              Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    cargo_grupo:          Mapped["CargoGrupo"] = db.relationship("CargoGrupo", back_populates='cargos')
    vinculos:      Mapped[List["Vinculo"]] = db.relationship("Vinculo", back_populates='cargo')