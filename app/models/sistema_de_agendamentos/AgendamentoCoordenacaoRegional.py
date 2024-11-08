# =================================================================================================================================================================
# Imports
# =================================================================================================================================================================

# Imports padrões
from datetime import time, datetime
from typing import TYPE_CHECKING

# Imports de terceiros
from sqlalchemy.orm import Mapped, mapped_column

# Imports locais
from app.config.db import db

# =================================================================================================================================================================
# Type para o mapping de colunas
# =================================================================================================================================================================

if TYPE_CHECKING:
    from app.models.base.CoordenacaoRegional import CoordenacaoRegional


# =================================================================================================================================================================
# Model de AgendamentoCoordenacaoRegional
# =================================================================================================================================================================

class AgendamentoCoordenacaoRegional(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_SISTEMA_AGENDAMENTOS_COORDENACOES_REGIONAIS'

    # Define as colunas da tabela
    id:                         Mapped[int] = mapped_column(primary_key=True)
    coordenacao_regional_id:    Mapped[int] = mapped_column(db.ForeignKey('SGDP_COORDENACOES_REGIONAIS.id'))
    horario:                    Mapped[time]
    vagas:                      Mapped[int]
    atualizado_em:              Mapped[datetime]    
    criado_em:                  Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    coordenacao_regional:       Mapped["CoordenacaoRegional"] = db.relationship("CoordenacaoRegional", back_populates='horarios_agendamento')