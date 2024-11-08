# =================================================================================================================================================================
# Imports
# =================================================================================================================================================================

# Imports padrões
from datetime import datetime
from typing import TYPE_CHECKING

# Imports de terceiros
from sqlalchemy.orm import Mapped, mapped_column

# Imports locais
from app.config.db import db

# =================================================================================================================================================================
# Type para o mapping de colunas
# =================================================================================================================================================================

if TYPE_CHECKING:
    from app.models.base.Unidade import Unidade
    from app.models.base.CoordenacaoRegional import CoordenacaoRegional
    from app.models.base.Municipio import Municipio

# =================================================================================================================================================================
# Model de UnidadeHistorico
# =================================================================================================================================================================

class UnidadeHistorico(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_UNIDADES_HISTORICO'

    # Define as colunas da tabela
    id:                         Mapped[int] = mapped_column(primary_key=True)
    unidade_id:                 Mapped[int] = mapped_column(db.ForeignKey('SGDP_UNIDADES.id'))
    coordenacao_regional_id:    Mapped[int] = mapped_column(db.ForeignKey('SGDP_COORDENACOES_REGIONAIS.id'))
    municipio_id:               Mapped[int] = mapped_column(db.ForeignKey('SGDP_MUNICIPIOS.id'))
    mdl:                        Mapped[str]
    inep:                       Mapped[str]
    nome_folha:                 Mapped[str]
    nome_analitico:             Mapped[str]
    caracteristica:             Mapped[str]
    tipo:                       Mapped[str]
    unidade_superior:           Mapped[str]
    atualizado_em:              Mapped[datetime]
    criado_em:                  Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    unidade:                    Mapped["Unidade"] = db.relationship("Unidade", back_populates='historico')
    coordenacao_regional:       Mapped["CoordenacaoRegional"] = db.relationship("CoordenacaoRegional", back_populates='unidades_historico')
    municipio:                  Mapped["Municipio"] = db.relationship("Municipio", back_populates='unidades_historico')