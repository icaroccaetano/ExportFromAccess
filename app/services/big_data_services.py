from app.config.db import db
from app.models.base.DadosConcurso import DadosPS2022
from app.models.base.Servidor import Servidor
from app.models.base.Vinculo import Vinculo
from datetime import datetime

def buscar_vinculos (cpf):                                                          
    servidor = Servidor.query.filter(Servidor.cpf == cpf)
    for vinculo in servidor.vinculos:
        if vinculo.data_inicio > datetime(2023, 1, 1) and vinculo.situacao_vinculo == "Efetivo / Empregado Público":
            return vinculo.vinculo
    
    return None

