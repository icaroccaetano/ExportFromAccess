# =================================================================================================================================================================
# Imports
# =================================================================================================================================================================

# Imports padrões
from typing import TYPE_CHECKING
from datetime import datetime

# Imports de terceiros
from sqlalchemy.orm import Mapped, mapped_column

# Imports locais
from app.config.db import db

# =================================================================================================================================================================
# Type para o mapping de colunas
# =================================================================================================================================================================

if TYPE_CHECKING:
    from app.models.base.Referencia import Referencia
    from app.models.base.Vinculo import Vinculo
    from app.models.base.Rubrica import Rubrica

# =================================================================================================================================================================
# Model de RubricaVinculo
# =================================================================================================================================================================

class RubricaVinculo(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_RUBRICAS_VINCULOS'

    # Define as colunas da tabela
    id:                 Mapped[int] = mapped_column(primary_key=True)
    referencia_id:      Mapped[int] = mapped_column(db.ForeignKey('SGDP_REFERENCIAS.id'))
    vinculo_id:         Mapped[int] = mapped_column(db.ForeignKey('SGDP_VINCULOS.id'))
    rubrica_id:         Mapped[int] = mapped_column(db.ForeignKey('SGDP_RUBRICAS.id'))
    valor:              Mapped[float]
    atualizado_em:      Mapped[datetime]
    criado_em:          Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    referencia:         Mapped["Referencia"] = db.relationship("Referencia", back_populates='rubricas_vinculos')
    vinculo:            Mapped["Vinculo"] = db.relationship("Vinculo", back_populates='rubricas_vinculos')
    rubrica:            Mapped["Rubrica"] = db.relationship("Rubrica", back_populates='rubricas_vinculos')