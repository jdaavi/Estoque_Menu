from flask import Flask, render_template, request, redirect, url_for, session
import hashlib
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Gera uma chave secreta aleatória

# Página inicial (Login)
@app.route('/')
def index():
    return render_template('index.html')  # O HTML da página de login

# Página de início (após login)
@app.route('/inicio')
def inicio():
    if 'hash' not in session:
        return redirect(url_for('index'))  # CORRIGIDO: Redirecionar para o login
    
    return render_template('inicio.html')

# Página de Estoque (após login)
@app.route('/estoque')
def estoque():
    if 'hash' not in session:
        return redirect(url_for('index'))  # CORRIGIDO
    
    return render_template('estoque.html')

# Página Financeiro (após login)
@app.route('/financeiro')
def financeiro():
    if 'hash' not in session:
        return redirect(url_for('index'))  # CORRIGIDO
    
    return render_template('financeiro.html')

@app.route('/transferencia')
def transferencia():
    return render_template('transferencia.html')

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

    # Simulação de autenticação (substitua por verificação real do banco de dados)
    if login == "Menu2025" and senha == "menu@2025":
        hash_value = hashlib.sha256(login.encode()).hexdigest()  # Cria um hash único
        session['user'] = login
        session['hash'] = hash_value
        return redirect(url_for('inicio'))  # Redireciona para a página inicial pós-login
    else:
        return "Usuário ou senha incorretos", 401  # Código 401 para indicar erro de autenticação

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
