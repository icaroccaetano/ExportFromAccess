# =================================================================================================================================================================
# Imports
# =================================================================================================================================================================

# Imports padrões
from datetime import datetime, date
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
    from app.models.base.Funcao import Funcao
    from app.models.base.Unidade import Unidade


# =================================================================================================================================================================
# Model de Aula
# =================================================================================================================================================================


class Aula(db.Model):
    # Define o nome da tabela no banco de dados
    __tablename__ = 'SGDP_AULAS'

    # Define as colunas da tabela
    id:                             Mapped[int] = mapped_column(primary_key=True)
    vinculo_id:                     Mapped[int] = mapped_column(db.ForeignKey('SGDP_VINCULOS.id'))
    funcao_id:                      Mapped[int] = mapped_column(db.ForeignKey('SGDP_FUNCOES.id'))
    unidade_id:                     Mapped[int] = mapped_column(db.ForeignKey('SGDP_UNIDADES.id'))
    codigo_composicao:              Mapped[int]
    composicao:                     Mapped[str]
    serie:                          Mapped[str]
    codigo_turma:                   Mapped[int]
    turma:                          Mapped[str]
    turno:                          Mapped[str]
    integral:                       Mapped[str]
    semestral:                      Mapped[str]
    codigo_disciplina:              Mapped[int]
    disciplina:                     Mapped[str]
    base_matriz:                    Mapped[str]
    codigo_area_do_conhecimento:    Mapped[int]
    area_do_conhecimento:           Mapped[str]
    carga_horaria_matriz:           Mapped[int]
    carga_horaria_aulas:            Mapped[int]
    carga_horaria_horas:            Mapped[float]
    substituicao:                   Mapped[str]
    fase:                           Mapped[str]
    ensino_modalidade:              Mapped[str]
    ensino_nivel:                   Mapped[str]
    data_inicio:                    Mapped[date]
    data_fim:                       Mapped[date]
    atualizado_em:                  Mapped[datetime]
    criado_em:                      Mapped[datetime]

# =================================================================================================================================================================
# Relacionamentos com as outras tabelas
# =================================================================================================================================================================

    vinculo:                        Mapped["Vinculo"] = db.relationship("Vinculo", back_populates='aulas')
    funcao:                         Mapped["Funcao"] = db.relationship("Funcao", back_populates='aulas')
    unidade:                        Mapped["Unidade"] = db.relationship("Unidade", back_populates='aulas')