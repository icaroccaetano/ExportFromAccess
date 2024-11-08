# =================================================================================================================================================================
# Imports
# =================================================================================================================================================================

# Imports padrões
from datetime import datetime
from typing import TYPE_CHECKING

# Imports de terceiros
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Imports locais
from app.config.db import db

# =================================================================================================================================================================
# Type para o mapping de colunas
# =================================================================================================================================================================

if TYPE_CHECKING:
    from app.models.sistema_de_acessos.Usuario import Usuario
    from app.models.sistema_de_acessos.Sistema import Sistema
    from app.models.sistema_de_acessos.NivelAcesso import NivelAcesso

# =================================================================================================================================================================
# Model de Acesso
# =================================================================================================================================================================

class Acesso(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_ACESSOS'

    # Define as colunas da tabela
    id:                 Mapped[int] = mapped_column(primary_key=True)
    usuario_id:         Mapped[int] = mapped_column(db.ForeignKey('SGDP_USUARIOS.id'))
    sistema_id:         Mapped[int] = mapped_column(db.ForeignKey('SGDP_SISTEMAS.id'))
    nivel_acesso_id:    Mapped[int] = mapped_column(db.ForeignKey('SGDP_NIVEIS_ACESSOS.id'))
    atualizado_em:      Mapped[datetime]
    criado_em:          Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    usuario:            Mapped["Usuario"] = db.relationship('Usuario', back_populates='acessos')
    sistema:            Mapped["Sistema"] = db.relationship('Sistema', back_populates='acessos')
    nivel_acesso:       Mapped["NivelAcesso"] = db.relationship('NivelAcesso', back_populates='acessos')