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
    from app.models.base.CoordenacaoRegional import CoordenacaoRegional
    from app.models.base.Municipio import Municipio
    from app.models.base.UnidadeHistorico import UnidadeHistorico
    from app.models.base.Modulacao import Modulacao
    from app.models.base.ModulacaoHistorico import ModulacaoHistorico
    from app.models.base.Aula import Aula

# =================================================================================================================================================================
# Model de Unidade
# =================================================================================================================================================================

class Unidade(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_UNIDADES'

    # Define as colunas da tabela
    id:                         Mapped[int] = mapped_column(primary_key=True)
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

    coordenacao_regional:       Mapped["CoordenacaoRegional"] = db.relationship("CoordenacaoRegional", back_populates='unidades')
    municipio:                  Mapped["Municipio"] = db.relationship("Municipio", back_populates='unidades')
    historico:                  Mapped[List["UnidadeHistorico"]] = db.relationship("UnidadeHistorico", back_populates='unidade')
    modulacoes_ativas:          Mapped[List["Modulacao"]] = db.relationship("Modulacao", back_populates='unidade')
    modulacoes_historico:       Mapped[List["ModulacaoHistorico"]] = db.relationship("ModulacaoHistorico", back_populates='unidade')
    aulas:                      Mapped[List["Aula"]] = db.relationship("Aula", back_populates='unidade')