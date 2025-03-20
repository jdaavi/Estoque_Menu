from flask import Flask, render_template, request, redirect, url_for, session,jsonify
import hashlib
import os
import requests
import redis



app = Flask(__name__)

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_KEY_PREFIX'] = 'sess:'
app.config['SESSION_REDIS'] = redis.StrictRedis(host='localhost', port=6379, db=0)

produtos = [
    {"n_ordem": "038", "data_compra": "02/03/2025", "entrega": "05/02/2025", "fornecedor": "Nagaura", "documento": "nfe-324", "recebimento": "06/02/2025", "destino": "Aldeota", "valor": "45,000.00", "categoria": "Hortifruti", "situacao": "Entregue", "valor_recebimento": "250.00", "situacao_compras": "Em aberto"},
    {"n_ordem": "039", "data_compra": "03/03/2025", "entrega": "06/02/2025", "fornecedor": "Nagaura", "documento": "nfe-123456", "recebimento": "07/02/2025", "destino": "Aldeota", "valor": "250.00", "categoria": "Hortifruti", "situacao": "Entregue", "valor_recebimento": "250.00", "situacao_compras": "Em aberto"},
]

# Página inicial (Login)
@app.route('/')
def index():
    return render_template('index.html')  # O HTML da página de login

# Página de início (após login)
@app.route('/inicio')
def inicio():
    if not 'token' or 'token' not in session:
        return redirect(url_for('index'))  # CORRIGIDO: Redirecionar para o login
    
    return render_template('inicio.html')

# Página de Estoque (após login)
@app.route('/estoque')
def estoque():
    if not 'token' or 'token' not in session:
        return redirect(url_for('index'))  # CORRIGIDO
    
    return render_template('estoque.html')

# Página Financeiro (após login)
@app.route('/financeiro')
def financeiro():
    if not 'token' or 'token' not in session:
        return redirect(url_for('index'))  # CORRIGIDO
    
    return render_template('financeiro.html')

@app.route('/transferencia')
def transferencia():
    return render_template('transferencia.html')

@app.route('/produtos')
def analise_produtos():
    if 'token' not in session:
        return redirect(url_for('index'))
    
    return render_template('produtos.html')

@app.route('/compras')
def compras():
    if 'token' not in session:
        return redirect(url_for('index'))
    
    return render_template('compras.html')

@app.route('/cadastro')
def cadastro():
    if 'token' not in session:
        return redirect(url_for('index'))
    
    return render_template('cadastro.html')

# Logout (Sair)
@app.route('/sair')
def sair():
    session.clear()  # Limpa a sessão ao sair
    return redirect(url_for('index'))  # CORRIGIDO
 
# Rota de Login
@app.route('/login', methods=['POST'])
def login():
    login = request.form['login']
    senha = request.form['senha']

    data = requests.request(method='POST',url='HTTP://10.10.10.10.107:5001/login',json={"username": login, "senha": senha})
    response_data = data.json()  # Converte para dicionário Python

    if data.status_code == 200:

        user_id = response_data['user_id']
        token = response_data['token']

        if not token:
            return jsonify({"error": "Falha ao obter token"}), 500

        session[user_id] = token  # Armazena o token na sessão Redis
        session['nivel'] = response_data['nivel']
        return redirect(url_for('inicio')) 
    
    if data.status_code == 404:
        return jsonify(data)
    
    if data.status_code == 401:
        return jsonify(data)
    


    # if login == 'Menu@2025' and senha == '123456':
    #     hash_value = hashlib.sha256((login+senha).encode()).hexdigest()
    #     session['user'] = login
    #     session['hash'] = hash_value
    #     return redirect(url_for('inicio')) 

    # else:
    #     return "usuario ou senha incorreta", 401


@app.route('/nova_compra', methods =['GET','POST'])
def nova_compra():
    if request.method == 'POST':

        n_ordem = request.form['n_ordem']
        data_compra = request.form['data_compra']
        entrega = request.form['entrega']
        fornecedor = request.form['fornecedor']
        documento = request.form['documento']
        recebimento = request.form['recebimento']
        destino = request.form['destino']
        valor = request.form['valor']
        categoria = request.form['categoria']
        situacao = request.form['situacao']
        valor_recebimento = request.form['valor_recebimento']
        situacao_compras = request.form['situacao_compras']

        # Adicionando a nova compra à lista de produtos
        nova_compra = {
            "n_ordem": n_ordem,
            "data_compra": data_compra,
            "entrega": entrega,
            "fornecedor": fornecedor,
            "documento": documento,
            "recebimento": recebimento,
            "destino": destino,
            "valor": valor,
            "categoria": categoria,
            "situacao": situacao,
            "valor_recebimento": valor_recebimento,
            "situacao_compras": situacao_compras
        }
        produtos.append(nova_compra)
        return redirect(url_for('compras'))

    return render_template('nova_compra.html')

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
