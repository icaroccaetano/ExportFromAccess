# =================================================================================================================================================================
# Imports
# =================================================================================================================================================================

# Imports padrões
from datetime import datetime, date
from typing import TYPE_CHECKING, List

# Imports de terceiros
from sqlalchemy.orm import Mapped, mapped_column

# Imports locais
from app.config.db import db

# =================================================================================================================================================================
# Type para o mapping de colunas
# =================================================================================================================================================================

if TYPE_CHECKING:
    from app.models.base.Servidor import Servidor
    from app.models.base.Cargo import Cargo
    from app.models.base.Modulacao import Modulacao
    from app.models.base.ModulacaoHistorico import ModulacaoHistorico
    from app.models.base.Aula import Aula
    from app.models.base.RubricaVinculo import RubricaVinculo
    from app.models.sistema_de_atualizacao_do_banco.SistemaAtualizacaoBancoLogVinculo import SistemaAtualizacaoBancoLogVinculo


# =================================================================================================================================================================
# Model de Vinculo
# =================================================================================================================================================================

class Vinculo(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_VINCULOS'

    # Define as colunas da tabela
    id:                           Mapped[int] = mapped_column(primary_key=True)
    vinculo:                      Mapped[str]
    servidor_id:                  Mapped[int] = mapped_column(db.ForeignKey('SGDP_SERVIDORES.id'))
    cargo_id:                     Mapped[int] = mapped_column(db.ForeignKey('SGDP_CARGOS.id'))
    situacao_vinculo:             Mapped[str]
    data_inicio:                  Mapped[date]
    data_fim:                     Mapped[date]
    atualizado_em:                Mapped[datetime]
    criado_em:                    Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    servidor:                     Mapped["Servidor"] = db.relationship("Servidor", back_populates='vinculos')
    cargo:                        Mapped["Cargo"] = db.relationship("Cargo", back_populates='vinculos')
    modulacoes_ativas:            Mapped[List["Modulacao"]] = db.relationship("Modulacao", back_populates='vinculo')
    modulacoes_historico:         Mapped[List["ModulacaoHistorico"]] = db.relationship("ModulacaoHistorico", back_populates='vinculo')
    aulas:                        Mapped[List["Aula"]] = db.relationship("Aula", back_populates='vinculo')
    rubricas_vinculos:            Mapped[List["RubricaVinculo"]] = db.relationship("RubricaVinculo", back_populates='vinculo')
    logs_vinculo:                 Mapped[List["SistemaAtualizacaoBancoLogVinculo"]] = db.relationship("SistemaAtualizacaoBancoLogVinculo", back_populates='vinculo')