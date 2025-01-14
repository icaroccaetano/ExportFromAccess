from app.database.access_db import get_df
from app.database.bigdata_db import get_engine
from sqlalchemy import text
from datetime import datetime

#from app.models.base.DadosConcurso import DadosPS2022

def main():
    dados_servidores = get_df("SELECT Nome_Canidato, CPF, Cidade, Cargo, AGENDAMENTO_TURMA, LISTA, VINCULO, DATA_EFETIVO_EXERCICIO, DATA_POSSE, PROCESSON FROM DADOS")
    engine = get_engine()
    i = 0
    with engine.connect() as connection:
        for dados_servidor in dados_servidores.itertuples():
            SQL_INSERT = str_form(dados_servidor) 
            i += 1
            try:
                # Executa o comando SQL no banco de dados MySQL
                connection.execute(text(SQL_INSERT))

                # Exibe progresso
                print(f"{i} de {len(dados_servidores)} - Inserido no banco")
            
            except Exception as e:
                # Exibe erro em caso de falha
                print(f"Erro ao inserir o registro {i}: {e}")
        connection.commit()
            

def str_form(dados_servidor):
    if not dados_servidor.PROCESSON:
        SQL = f"""
        INSERT INTO SGDP_SISTEMA_REGISTRO_DE_ADMISSAO 
        (nome, cpf, regiao, materia, turma, lista) 
        VALUES 
        ('{dados_servidor.Nome_Canidato}','{dados_servidor.CPF}', '{dados_servidor.Cidade}','{dados_servidor.Cargo}','{dados_servidor.AGENDAMENTO_TURMA}',{dados_servidor.LISTA})
        """
    elif not dados_servidor.DATA_POSSE: #se nao tem uma das datas tem a outra 
        SQL = f"""
        INSERT INTO SGDP_SISTEMA_REGISTRO_DE_ADMISSAO 
        (nome, cpf, regiao, materia, turma, lista, processo_sei) 
        VALUES 
        ('{dados_servidor.Nome_Canidato}','{dados_servidor.CPF}', '{dados_servidor.Cidade}','{dados_servidor.Cargo}','{dados_servidor.AGENDAMENTO_TURMA}',{dados_servidor.LISTA},'{dados_servidor.PROCESSON}')
        """

    

    return SQL

if __name__ == "__main__":
    main()