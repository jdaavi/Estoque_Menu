import psycopg2
import os
from psycopg2 import sql

class Connection:
    def __init__(self, my_host, db_name, my_user, my_password):
        self.my_host = my_host
        self.db_name = db_name
        self.my_user = my_user
        self.my_password = my_password
        self.con = None
        self.cur = None

    def connect(self):
        """Estabelece a conexão com o banco de dados"""
        try:
            self.con = psycopg2.connect(
                host=self.my_host,
                database=self.db_name,
                user=self.my_user,
                password=self.my_password
            )
            self.cur = self.con.cursor()
        except Exception as e:
            print(f"Erro ao conectar no banco de dados: {e}")
            raise

    def close(self):
        """Fecha a conexão com o banco de dados"""
        if self.cur:
            self.cur.close()
        if self.con:
            self.con.close()

# Usando a classe Connection em seu código
def get_connection():
    return Connection(
        my_host=os.getenv('HOST'),
        db_name=os.getenv('DB_NAME'),
        my_user=os.getenv('USER'),
        my_password=os.getenv('PASSWORD')
    )

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
     