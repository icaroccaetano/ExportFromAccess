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

# =================================================================================================================================================================
# Model de Endereco
# =================================================================================================================================================================

class Endereco(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_ENDERECOS'

    # Define as colunas da tabela
    id:                         Mapped[int] = mapped_column(primary_key=True)
    servidor_id:                Mapped[int] = mapped_column(db.ForeignKey('SGDP_SERVIDORES.id'))
    tipo_logradouro:            Mapped[str]
    nome_logradouro:            Mapped[str]
    informacao_complementar:    Mapped[str]
    numero_imovel:              Mapped[str]
    quadra:                     Mapped[str]
    lote:                       Mapped[str]
    bairro:                     Mapped[str]
    municipio:                  Mapped[str]
    uf:                         Mapped[str]
    cep:                        Mapped[str]
    atualizado_em:              Mapped[datetime]
    criado_em:                  Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    servidor:                   Mapped["Servidor"] = db.relationship("Servidor", back_populates='enderecos')