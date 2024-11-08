# =================================================================================================================================================================
# Imports
# =================================================================================================================================================================

# Imports padrões
from datetime import datetime
from typing import TYPE_CHECKING, List

# Imports de terceiros
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column

# Imports locais
from app.config.db import db

# =================================================================================================================================================================
# Type para o mapping de colunas
# =================================================================================================================================================================

if TYPE_CHECKING:
    from app.models.base.Servidor import Servidor
    from app.models.sistema_de_acessos.Acesso import Acesso

# =================================================================================================================================================================
# Model de Usuario
# =================================================================================================================================================================

class Usuario(db.Model, UserMixin):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_USUARIOS'

    # Define as colunas da tabela
    id:                 Mapped[int] = mapped_column(primary_key=True)
    servidor_id:        Mapped[int] = mapped_column(db.ForeignKey('SGDP_SERVIDORES.id'))
    hash_senha:         Mapped[str]
    atualizado_em:      Mapped[datetime]
    criado_em:          Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    servidor:           Mapped["Servidor"] = db.relationship('Servidor', back_populates='usuario')
    acessos:            Mapped[List["Acesso"]] = db.relationship('Acesso', back_populates='usuario')