import psycopg2
from psycopg2 import sql

def create_db():
    conn = psycopg2.connect(
        dbname = "datalake_menu",
        user = "datalake_menu",
        password = "Acesso1!",
        host = "datalake_menu.postgresql.dbaas.com.br",
        port = "5432",
    )
    cursor = conn.cursor()

    cursor.execute("""
         CREATE TABLE IF NOT EXISTS funcionarios (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100),
            cargo VARCHAR(100),
            setor VARCHAR(100),
            email VARCHAR(100),
            telefone VARCHAR(15),
            cpf VARCHAR(14),
            data_nascimento DATE,
            data_contrato DATE
        )
    """)
    conn.commit()
    conn.close()

def add_funcionario(nome, cargo, setor, email, telefone, cpf, data_nascimento, data_contrato):
    conn = psycopg2.connect(
            dbname = "datalake_menu",
            user = "datalake_menu",
            password = "Acesso1!",
            host = "datalake_menu.postgresql.dbaas.com.br",
            port = "5432",
    )
    cursor = conn.cursor()

    cursor.execute("""
         INSERT INTO funcionarios (nome, cargo, setor, email, telefone, cpf, data_nascimento, data_contrato)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (nome, cargo, setor, email, telefone, cpf, data_nascimento, data_contrato))

    conn.commit()
    conn.close()

def get_funcionarios():
    conn = psycopg2.connect(
        dbname="funcionarios_db",  
        user="seu_usuario",        
        password="sua_senha",      
        host="localhost",          
        port="5432"                
    )
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    conn.close()
    
    return funcionarios
     