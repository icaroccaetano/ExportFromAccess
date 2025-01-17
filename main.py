from app.database.access_db import get_df
from app.database.bigdata_db import get_engine
from sqlalchemy import text
from datetime import datetime
import pandas as pd

def main():
    dados_servidores = get_df("SELECT Nome_Canidato, CPF, Cidade, Cargo, AGENDAMENTO_TURMA, LISTA, VINCULO, DATA_EFETIVO_EXERCICIO, DATA_POSSE, PROCESSON FROM DADOS WHERE LISTA = 1 OR LISTA = 2")
    engine = get_engine()
    i = 0
    errcount = 0
    with engine.connect() as connection:
        for dados_servidor in dados_servidores.itertuples():
            SQL_INSERT, params = sql_form(dados_servidor) 
            i += 1
            try:
                # Executa o comando SQL no banco de dados MySQL
                connection.execute(text(SQL_INSERT), params)

                # Exibe progresso
                print(f"{i} de {len(dados_servidores)} - Inserido no banco")
            
            except Exception as e:
                # Exibe erro em caso de falha
                print(f"Erro ao inserir o registro {i}: {e}")
                errcount += 1
        connection.commit()
    print(f"Concluido. Total de erros: {errcount}")
            

def sql_form(dados_servidor):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    params = {
        "nome": dados_servidor.Nome_Canidato,
        "cpf": dados_servidor.CPF,
        "regiao": dados_servidor.Cidade,
        "materia": dados_servidor.Cargo,
        "turma": dados_servidor.AGENDAMENTO_TURMA,
        "lista": dados_servidor.LISTA,
        "processo_sei": dados_servidor.PROCESSON,
        "data_inicio": dados_servidor.DATA_EFETIVO_EXERCICIO,
        "data_posse": dados_servidor.DATA_POSSE,
        "vinculo": dados_servidor.VINCULO,
        "atualizado_em": now,
        "criado_em": now,
    }
    if not dados_servidor.PROCESSON: #nao tem processo nao tem mais nada
        SQL = f"""
        INSERT INTO SGDP_SISTEMA_REGISTRO_DE_ADMISSAO_TCE 
        (nome, cpf, regiao, materia, turma, lista, atualizado_em, criado_em) 
        VALUES 
        (:nome, :cpf, :regiao, :materia, :turma, :lista, :atualizado_em, :criado_em) 
        """
    elif not dados_servidor.DATA_POSSE or pd.isna(dados_servidor.DATA_POSSE): #se nao tem uma das datas nao tem a outra nem o vinculo
        SQL = f"""
        INSERT INTO SGDP_SISTEMA_REGISTRO_DE_ADMISSAO_TCE 
        (nome, cpf, regiao, materia, turma, lista, processo_sei, atualizado_em, criado_em) 
        VALUES 
        (:nome, :cpf, :regiao, :materia, :turma, :lista, :processo_sei, :atualizado_em, :criado_em)
        """
    elif not dados_servidor.VINCULO: #tem as duas datas -> Sem vinculo
        SQL = f"""
        INSERT INTO SGDP_SISTEMA_REGISTRO_DE_ADMISSAO_TCE 
        (nome, cpf, regiao, materia, turma, lista, processo_sei, data_inicio, data_posse, atualizado_em, criado_em) 
        VALUES 
        (:nome, :cpf, :regiao, :materia, :turma, :lista, :processo_sei, :data_inicio, :data_posse, :atualizado_em, :criado_em) 
        """
    else: #tem as duas datas -> Com vinculo
        SQL = f"""
        INSERT INTO SGDP_SISTEMA_REGISTRO_DE_ADMISSAO_TCE 
        (nome, cpf, regiao, materia, turma, lista, processo_sei, data_inicio, data_posse, vinculo, atualizado_em, criado_em) 
        VALUES 
        (:nome, :cpf, :regiao, :materia, :turma, :lista, :processo_sei, :data_inicio, :data_posse, :vinculo, :atualizado_em, :criado_em) 
        """
    return SQL, params

if __name__ == "__main__":
    main()