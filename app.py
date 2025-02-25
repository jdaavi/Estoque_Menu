from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página inicial (Login)
@app.route('/')
def index():
    return render_template('index.html')  # O HTML que você já criou

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

# Página de Estoque (após inicio)
@app.route('/estoque')
def estoque():
    return render_template('estoque.html')  # A página de Estoque que você já criou

@app.route('/financeiro')
def financeiro():
    return render_template('financeiro.html')

@app.route('/sair')
def sair():
    return redirect(url_for('inicio'))

# Rota de Login
@app.route('/login', methods=['POST'])
def login():
    login = request.form['login']
    senha = request.form['senha']

    # Aqui você pode adicionar a lógica para autenticar o usuário
    # Para fins de exemplo, vamos apenas fazer um check simples
    if login == "Menu2025" and senha == "menu@2025":
        return redirect(url_for('inicio'))  # Redireciona para a página de inicio
    else:
        return "Usuário ou senha incorretos"  # Exibe erro em caso de falha no login
    

if __name__ == '__main__':
    app.run(host='10.10.10.194', port=5000, debug=True)
