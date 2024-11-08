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
    from app.models.base.Modulacao import Modulacao
    from app.models.base.ModulacaoHistorico import ModulacaoHistorico
    from app.models.base.Aula import Aula

# =================================================================================================================================================================
# Model de Funcao
# =================================================================================================================================================================

class Funcao(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_FUNCOES'

    # Define as colunas da tabela
    id:                         Mapped[int] = mapped_column(primary_key=True)
    descricao:                  Mapped[str]
    classificacao:              Mapped[str]
    data_inicio_da_vigencia:    Mapped[date]
    data_fim_da_vigencia:       Mapped[date]
    atualizado_em:              Mapped[datetime]
    criado_em:                  Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    modulacoes_ativas:          Mapped[List["Modulacao"]] = db.relationship("Modulacao", back_populates='funcao')
    modulacoes_historico:       Mapped[List["ModulacaoHistorico"]] = db.relationship("ModulacaoHistorico", back_populates='funcao')
    aulas:                      Mapped[List["Aula"]] = db.relationship("Aula", back_populates='funcao')