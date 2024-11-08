# =================================================================================================================================================================
# Imports
# =================================================================================================================================================================

# Imports padrões
from typing import TYPE_CHECKING, List
from datetime import datetime

# Imports de terceiros
from sqlalchemy.orm import Mapped, mapped_column

# Imports locais
from app.config.db import db

# =================================================================================================================================================================
# Type para o mapping de colunas
# =================================================================================================================================================================

if TYPE_CHECKING:
    from app.models.base.CoordenacaoRegional import CoordenacaoRegional
    from app.models.base.Unidade import Unidade
    from app.models.base.UnidadeHistorico import UnidadeHistorico

# =================================================================================================================================================================
# Model de Municipio
# =================================================================================================================================================================

class Municipio(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_MUNICIPIOS'

    # Define as colunas da tabela
    id:                         Mapped[int] = mapped_column(primary_key=True)
    nome:                       Mapped[str]
    coordenacao_regional_id:    Mapped[int] = mapped_column(db.ForeignKey('SGDP_COORDENACOES_REGIONAIS.id'))
    atualizado_em:              Mapped[datetime]
    criado_em:                  Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    coordenacao_regional:       Mapped["CoordenacaoRegional"] = db.relationship("CoordenacaoRegional", back_populates='municipios')
    unidades:                   Mapped[List["Unidade"]] = db.relationship("Unidade", back_populates='municipio')
    unidades_historico:         Mapped[List["UnidadeHistorico"]] = db.relationship("UnidadeHistorico", back_populates='municipio')