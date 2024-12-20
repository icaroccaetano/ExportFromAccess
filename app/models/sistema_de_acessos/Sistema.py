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
    from app.models.sistema_de_acessos.Sistema import Sistema

# =================================================================================================================================================================
# Model de NivelAcesso
# =================================================================================================================================================================

class Sistema(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_SISTEMAS'

    # Define as colunas da tabela
    id:                 Mapped[int] = mapped_column(primary_key=True)
    nome:               Mapped[str]
    versao:             Mapped[str]
    atualizado_em:      Mapped[datetime]
    criado_em:          Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    acessos = db.relationship('Acesso', back_populates='sistema')