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
    from app.models.base.Unidade import Unidade
    from app.models.base.UnidadeHistorico import UnidadeHistorico
    from app.models.base.Municipio import Municipio
    from app.models.sistema_de_agendamentos.Agendamento import Agendamento
    from app.models.sistema_de_agendamentos.AgendamentoCoordenacaoRegional import AgendamentoCoordenacaoRegional

# =================================================================================================================================================================
# Model de CoordenacaoRegional
# =================================================================================================================================================================
class CoordenacaoRegional(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_COORDENACOES_REGIONAIS'

    # Define as colunas da tabela
    id:                         Mapped[int] = mapped_column(primary_key=True)
    nome:                       Mapped[str]
    atualizado_em:              Mapped[datetime]
    criado_em:                  Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    horarios_agendamento:       Mapped["AgendamentoCoordenacaoRegional"] = db.relationship("AgendamentoCoordenacaoRegional", back_populates='coordenacao_regional')
    unidades:                   Mapped[List["Unidade"]] = db.relationship("Unidade", back_populates='coordenacao_regional')
    unidades_historico:         Mapped[List["UnidadeHistorico"]] = db.relationship("UnidadeHistorico", back_populates='coordenacao_regional')
    agendamentos:               Mapped[List["Agendamento"]] = db.relationship("Agendamento", back_populates='coordenacao_regional')
    municipios:                 Mapped[List["Municipio"]] = db.relationship("Municipio", back_populates='coordenacao_regional')