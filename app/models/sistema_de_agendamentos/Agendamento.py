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
    from app.models.base.Servidor import Servidor
    from app.models.base.CoordenacaoRegional import CoordenacaoRegional

# =================================================================================================================================================================
# Model de Agendamento
# =================================================================================================================================================================

class Agendamento(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_SISTEMA_AGENDAMENTOS_AGENDAMENTOS'

    # Define as colunas da tabela
    id:                         Mapped[int] = mapped_column(primary_key=True)
    servidor_id:                Mapped[int] = mapped_column(db.ForeignKey('SGDP_SERVIDORES.id'))
    coordenacao_regional_id:    Mapped[int] = mapped_column(db.ForeignKey('SGDP_COORDENACOES_REGIONAIS.id'))
    data_agendamento:           Mapped[datetime]
    descricao:                  Mapped[str]
    status:                     Mapped[str]
    atualizado_em:              Mapped[datetime]
    criado_em:                  Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    servidor:                   Mapped["Servidor"] = db.relationship("Servidor", back_populates='agendamentos')
    coordenacao_regional:       Mapped["CoordenacaoRegional"] = db.relationship("CoordenacaoRegional", back_populates='agendamentos')