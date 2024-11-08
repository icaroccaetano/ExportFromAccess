from datetime import datetime

# Imports de terceiros
from sqlalchemy.orm import Mapped, mapped_column

# Imports locais
from app.config.db import db
from app.models.base.Servidor import Servidor

class DadosPS2022(db.Model):
    __tablename__ = 'SGDP_SISTEMA_CONCURSO_PROCESSOS'

    referencia:     Mapped[str]
    vinculo_id:     Mapped[int] = mapped_column(db.ForeignKey('vinculo.id'))
    processo:       Mapped[str]
    cpf:            Mapped[str]
    nome:           Mapped[str]
    status_grad:    Mapped[str]
    status_ged:     Mapped[str]
    atualizado_em:  Mapped[datetime]
    criado_em:      Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    servidor:       Mapped["Servidor"] = db.relationship("Servidor", back_populates='vinculos')