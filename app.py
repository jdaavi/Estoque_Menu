from flask import Flask, render_template, request, redirect, url_for, session,jsonify, make_response
from flask_session import Session
from functools import wraps
import hashlib
import os
import requests
import redis
import dotenv

dotenv.load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave_super_secreta')  # Define a chave secreta

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_KEY_PREFIX'] = 'sess:'
app.config['SESSION_REDIS'] = redis.StrictRedis(host=str(os.getenv('REDIS_HOST')),port=int(os.getenv('REDIS_PORT')), db=int(os.getenv('REDIS_DB')))

Session(app)

produtos = [
    {"n_ordem": "038", "data_compra": "02/03/2025", "entrega": "05/02/2025", "fornecedor": "Nagaura", "documento": "nfe-324", "recebimento": "06/02/2025", "destino": "Aldeota", "valor": "45,000.00", "categoria": "Hortifruti", "situacao": "Entregue", "valor_recebimento": "250.00", "situacao_compras": "Em aberto"},
    {"n_ordem": "039", "data_compra": "03/03/2025", "entrega": "06/02/2025", "fornecedor": "Nagaura", "documento": "nfe-123456", "recebimento": "07/02/2025", "destino": "Aldeota", "valor": "250.00", "categoria": "Hortifruti", "situacao": "Entregue", "valor_recebimento": "250.00", "situacao_compras": "Em aberto"},
]

def verificacao_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Pega o token dos cookies
        auth_token = request.cookies.get("auth_token")
        
        # Verifica se o token está presente
        if not auth_token:
            return jsonify({"error": "Token ausente"}), 401

        # Faz a requisição para o serviço de validação de token, passando o token no header Authorization
        response_data = requests.post('http://10.10.10.107:5001/auth/validacao_token',
                                      headers={'Authorization': 'Bearer ' + auth_token})

        # Verifica a resposta do serviço de validação de token
        if response_data.status_code == 200:
            return func(*args, **kwargs)  # Se o token for válido, chama a função original
        else:
            data = response_data.json()
            msg = data.get('msg', "error")
            return jsonify({"msg":msg}),400

    return wrapper

def consultar_empresa(id_empresa):

    auth_token = request.cookies.get("auth_token")

    # URL corrigida (incluindo aspas para a URL correta)
    url = f"http://10.10.10.107:5001/empresa/{id_empresa}"
    
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    # Fazendo a requisição GET
    response_consulta = requests.get(url, headers=headers)

    # Verificando o código de status da resposta
    if response_consulta.status_code == 200:
        dados_empresa = response_consulta.json()  # Extrai os dados da resposta
        return dados_empresa
    elif response_consulta.status_code == 401:
        return {"erro": "Erro de autenticação. Verifique o token."}
    else:
        return {"erro": "Empresa não encontrada ou não existe."}
    
def deletar_empresa(id_empresa):
      
     auth_token = request.cookies.get("auth_token")

     url =  f"http://10.10.10.107:5001/empresa/{id_empresa}"
     headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
     
     response_deletar = requests.delete(url, headers=headers)

     if response_deletar.status_code == 200:
            return {"sucesso": "Empresa deletada com sucesso!"}
     elif response_deletar.status_code == 401:
            return {"erro": "Erro de autenticação. Verifique o token."}
     else:
            return {"erro": f"Erro no processo: {response_deletar.json().get('msg', 'Erro desconhecido')}"}

def atualizar_empresa(id_empresa, dados_atuais):
     
     auth_token = request.cookies.get("auth_token")

     url = f"http://10.10.10.107:5001/empresa/{id_empresa}"
     headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    
     response_atualizar = requests.patch(url, json=dados_atuais, headers=headers)

     if response_atualizar.status_code == 200:
        return {"sucesso": "Empresa atualizada com sucesso!"}
     elif response_atualizar.status_code == 400:
        return {"erro": f"Erro no processo: {response_atualizar.json().get('msg', 'Erro desconhecido')}"}
     else:
        return {"erro": f"Erro inesperado: {response_atualizar.status_code}"}
     

# Página inicial (Login)
@app.route('/')
def index():
    return render_template('login/index.html')  # O HTML da página de login

# Página de início (após login)
@app.route('/inicio')
@verificacao_token
def inicio():
    return render_template('login/inicio.html')

# Página de Estoque (após login)
@app.route('/estoque')
@verificacao_token
def estoque():  
    return render_template('estoque/estoque.html')

# Página Financeiro (após login)
@app.route('/financeiro')
@verificacao_token
def financeiro():
    return render_template('financeiro/financeiro.html')

@app.route('/transferencia')
@verificacao_token
def transferencia():
    return render_template('financeiro/transferencia.html')

@app.route('/produtos')
@verificacao_token
def analise_produtos():   
    return render_template('estoque/produtos.html')

@app.route('/compras')
@verificacao_token
def compras():   
    return render_template('compras/compras.html')

@app.route('/cadastro')
@verificacao_token
def cadastro():
    return render_template('estoque/cadastro.html')


@app.route('/usuario')
@verificacao_token
def usuario():
    return render_template('rh/rh.html')

@app.route('/funcionario')
@verificacao_token
def funcionario():
    return render_template('rh/funcionarios.html')

@app.route('/registro')
@verificacao_token
def registro():
    return render_template('rh/registro.html')

# Logout (Sair)
@app.route('/sair')
def sair():
    session.clear()  # Limpa a sessão ao sair
    return redirect(url_for('index'))  # CORRIGIDO
 
@app.route('/listar_empresas')

# Rota de Login
@app.route('/login', methods=['POST'])
def login():
    login = request.form['login']
    senha = request.form['senha']

    if not login or not senha:
        return jsonify({"error": "Campos login e senha são obrigatórios"}), 400

    response_data = requests.post('http://10.10.10.107:5001/oath', json={"username": login, "senha": senha})

    if response_data.status_code == 200:
        data = response_data.json()  # Converte a resposta para dicionário

        token = data.get('token')
        nivel = data.get('nivel')
        user_id = data.get('user_id')

        if not token:
            return jsonify({"error": "Falha ao obter token"}), 500

        # Armazena informações nos cookies
        response = make_response(redirect(url_for('inicio')) ,302)
        
        response.set_cookie(
        "auth_token", str(token),
        httponly=True,  # Protege contra JavaScript
        samesite="Strict",  # Restringe envio do cookie
        )

        response.set_cookie(
        "nivel",str(nivel),
        httponly=True,  # Protege contra JavaScript
        samesite="Strict",  # Restringe envio do cookie
        )

        return response

    if response_data.status_code in [401, 404]:
        data = response_data.json()  # Converte a resposta para dicionário    
        menssage = data.get('error', "Erro desconhecido")
        return jsonify({"error": menssage}), response.status_code     

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

    return render_template('compras/nova_compra.html')

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run()
