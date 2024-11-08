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
    from app.models.base.Vinculo import Vinculo
    from app.models.base.Funcao import Funcao
    from app.models.base.Unidade import Unidade

# =================================================================================================================================================================
# Model de Modulacao
# =================================================================================================================================================================

class Modulacao(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_MODULACOES_ATIVAS'

    # Define as colunas da tabela
    id:                 Mapped[int] = mapped_column(primary_key=True)
    vinculo_id:         Mapped[int] = mapped_column(db.ForeignKey('SGDP_VINCULOS.id'))
    funcao_id:          Mapped[int] = mapped_column(db.ForeignKey('SGDP_FUNCOES.id'))
    unidade_id:         Mapped[int] = mapped_column(db.ForeignKey('SGDP_UNIDADES.id'))
    carga_horaria:      Mapped[float]
    data_inicio:        Mapped[date]
    data_fim:           Mapped[date]
    atualizado_em:      Mapped[datetime]
    criado_em:          Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    vinculo:            Mapped["Vinculo"] = db.relationship("Vinculo", back_populates='modulacoes_ativas')
    funcao:             Mapped["Funcao"] = db.relationship("Funcao", back_populates='modulacoes_ativas')
    unidade:            Mapped["Unidade"] = db.relationship("Unidade", back_populates='modulacoes_ativas')