# =================================================================================================================================================================
# Imports
# =================================================================================================================================================================

# Imports padrões
from datetime import datetime

# Imports de terceiros
from sqlalchemy.orm import Mapped, mapped_column

# Imports locais
from app.config.db import db

# =================================================================================================================================================================
# Model de Atualizacao
# =================================================================================================================================================================

class Atualizacao(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_SISTEMA_ATUALIZACAO_BANCO_ATUALIZACOES'

    # Define as colunas da tabela
    id:                     Mapped[int] = mapped_column(primary_key=True)
    tabela:                 Mapped[str]
    ultima_atualizacao:     Mapped[datetime]
    atualizado_em:          Mapped[datetime]
    criado_em:              Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================
