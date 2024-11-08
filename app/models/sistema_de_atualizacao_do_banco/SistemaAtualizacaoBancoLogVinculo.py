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
    from app.models.base.Vinculo import Vinculo

# =================================================================================================================================================================
# Model de SistemaAtualizacaoBancoLogVinculo
# =================================================================================================================================================================
class SistemaAtualizacaoBancoLogVinculo(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_SISTEMA_ATUALIZACAO_BANCO_LOG_VINCULOS'

    # Define as colunas da tabela
    id:                     Mapped[int] = mapped_column(primary_key=True)
    vinculo_id:             Mapped[int] = mapped_column(db.ForeignKey('SGDP_VINCULOS.id'))
    mensagem:               Mapped[str]
    atualizado_em:          Mapped[datetime]
    criado_em:              Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    vinculo:                Mapped["Vinculo"] = db.relationship("Vinculo", back_populates='logs_vinculo')