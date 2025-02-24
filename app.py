from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página inicial (Login)
@app.route('/')
def index():
    return render_template('index.html')  # O HTML que você já criou

# Página de Estoque (após login)
@app.route('/estoque')
def estoque():
    return render_template('estoque.html')  # A página de Estoque que você já criou

# Rota de Login
@app.route('/login', methods=['POST'])
def login():
    login = request.form['login']
    senha = request.form['senha']

    # Aqui você pode adicionar a lógica para autenticar o usuário
    # Para fins de exemplo, vamos apenas fazer um check simples
    if login == "Menu2025" and senha == "menu@2025":
        return redirect(url_for('estoque'))  # Redireciona para a página de Estoque
    else:
        return "Usuário ou senha incorretos"  # Exibe erro em caso de falha no login

if __name__ == '__main__':
    app.run(host='10.10.10.107', port=5000, debug=True)
