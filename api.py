from flask import Flask, request, jsonify
from conn_database import Connection
from psycopg2 import sql as sql_pg
import os
from dotenv import load_dotenv

load_dotenv()

db = Connection(os.getenv("HOST"),os.getenv("DB_NAME"),os.getenv("USER"),os.getenv("PASSWORD"))

app = Flask("__name__")

@app.route("/verif_login",methods="POST")
def busca_usuario():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Dados não fornecidos ou formato inválido"}), 400
    
    password = data.get("password")

    verif = db.read_db(os.getenv("SCHEMA"),"usuarios",f"usuarios = {data.get("user")}")








    
