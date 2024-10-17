from app.database.access_db import get_df
from app.database.bigdata_db import get_engine
from sqlalchemy import text

def main():
    dados_servidores = get_df("SELECT * FROM DadosServidor")
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
    if dados_servidor.Admitido:
        adm = 1
    else:
        adm = 0
    
    if dados_servidor.Status and dados_servidor.ProcessoSEI:
        SQL = f"INSERT INTO SGDP_DADOS_PS2022 (nome, cpf, processo, status, admitido) VALUES ('{dados_servidor.Nome}','{dados_servidor.CPF}', '{dados_servidor.ProcessoSEI}', '{dados_servidor.Status}', {adm})"
    elif dados_servidor.Status:
        SQL = f"INSERT INTO SGDP_DADOS_PS2022 (nome, cpf, status, admitido) VALUES ('{dados_servidor.Nome}','{dados_servidor.CPF}', '{dados_servidor.Status}', {adm})"
    elif dados_servidor.ProcessoSEI:
        SQL = f"INSERT INTO SGDP_DADOS_PS2022 (nome, cpf, processo, admitido) VALUES ('{dados_servidor.Nome}','{dados_servidor.CPF}', '{dados_servidor.ProcessoSEI}', {adm})"
    else:
        SQL = f"INSERT INTO SGDP_DADOS_PS2022 (nome, cpf, admitido) VALUES ('{dados_servidor.Nome}','{dados_servidor.CPF}', {adm})"
    return SQL

if __name__ == "__main__":
    main()