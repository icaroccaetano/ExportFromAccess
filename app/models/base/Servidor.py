# =================================================================================================================================================================
# Imports
# =================================================================================================================================================================

# Imports padrões
from typing import TYPE_CHECKING, List
from datetime import datetime, date

# Imports de terceiros
from sqlalchemy.orm import Mapped, mapped_column

# Imports locais
from app.config.db import db

# =================================================================================================================================================================
# Type para o mapping de colunas
# =================================================================================================================================================================

if TYPE_CHECKING:
    from app.models.sistema_de_acessos.Usuario import Usuario
    from app.models.base.Endereco import Endereco
    from app.models.base.Contato import Contato
    from app.models.base.Vinculo import Vinculo
    from app.models.sistema_de_agendamentos.Agendamento import Agendamento
    from app.models.base.DadosConcurso import DadosPS2022
    

# =================================================================================================================================================================
# Model de Servidor
# =================================================================================================================================================================

class Servidor(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_SERVIDORES'

    # Define as colunas da tabela
    id:                 Mapped[int] = mapped_column(primary_key=True)
    cpf:                Mapped[str] = mapped_column(unique=True)
    nome:               Mapped[str]
    data_nascimento:    Mapped[date]
    sexo:               Mapped[str]
    rg:                 Mapped[str]
    escolaridade:       Mapped[str]
    nome_mae:           Mapped[str]
    atualizado_em:      Mapped[datetime]
    criado_em:          Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    usuario:           Mapped["Usuario"] = db.relationship("Usuario", back_populates='servidor')
    enderecos:         Mapped[List["Endereco"]] = db.relationship("Endereco", back_populates='servidor')
    contatos:          Mapped[List["Contato"]] = db.relationship("Contato", back_populates='servidor')
    vinculos:          Mapped[List["Vinculo"]] = db.relationship("Vinculo", back_populates='servidor')
    agendamentos:      Mapped[List["Agendamento"]] = db.relationship("Agendamento", back_populates='servidor')
    DadosPS2022:       Mapped[List["DadosPS2022"]] = db.relationship("DadosPS2022", back_populates='servidor')