from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

usuarios = []
current_id = 1

@app.route('/users', methods=['POST'])
def criar_usuario():
    """
    Cria um novo usuário.
    ---
    tags:
      - Usuários
    description: Cria um novo usuário com nome e email.
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: body
        name: user
        description: Objeto JSON com os dados do usuário
        required: true
        schema:
          type: object
          required:
            - nome
            - email
          properties:
            nome:
              type: string
              example: João Silva
            email:
              type: string
              example: joao@email.com
    responses:
      201:
        description: Usuário criado com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            nome:
              type: string
              example: João Silva
            email:
              type: string
              example: joao@email.com
      400:
        description: Requisição inválida, faltando nome ou email
        schema:
          type: object
          properties:
            erro:
              type: string
              example: "Nome e email são obrigatórios."
    """
    global current_id
    dados = request.json

    if not dados:
        return jsonify({'erro': 'Preencha todos os campos'}), 400

    if 'nome' not in dados or dados['nome'] == '':
        return jsonify({'erro': 'Digite seu nome'}), 400

    if 'email' not in dados or dados['email'] == '':
        return jsonify({'erro': 'Digite seu email'}), 400

    novo_usuario = {
        'id': current_id,
        'nome': dados['nome'],
        'email': dados['email']
    }

    usuarios.append(novo_usuario)
    current_id += 1

    return jsonify(novo_usuario), 201

@app.route('/users', methods=['GET'])
def listar_usuarios():
    """
    Lista todos os usuários.
    ---
    tags:
      - Usuários
    responses:
      200:
        description: Lista de usuários
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              nome:
                type: string
                example: João Silva
              email:
                type: string
                example: joao@email.com
    """
    return jsonify(usuarios), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def buscar_usuario_por_id(user_id):
    """
    Busca um usuário pelo ID.
    ---
    tags:
      - Usuários
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID do usuário
    responses:
      200:
        description: Usuário encontrado
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            nome:
              type: string
              example: João Silva
            email:
              type: string
              example: joao@email.com
      404:
        description: Usuário não encontrado
        schema:
          type: object
          properties:
            erro:
              type: string
              example: Usuário não encontrado
    """
    for usuario in usuarios:
        if usuario['id'] == user_id:
            return jsonify(usuario), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def atualizar_usuario(user_id):
    """
    Atualiza os dados de um usuário.
    ---
    tags:
      - Usuários
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID do usuário a ser atualizado
      - in: body
        name: user
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              example: Novo Nome
            email:
              type: string
              example: novo@email.com
    responses:
      200:
        description: Usuário atualizado com sucesso
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            nome:
              type: string
              example: Novo Nome
            email:
              type: string
              example: novo@email.com
      404:
        description: Usuário não encontrado
        schema:
          type: object
          properties:
            erro:
              type: string
              example: Usuário não encontrado
    """
    dados = request.json

    for usuario in usuarios:
        if usuario['id'] == user_id:
            usuario['nome'] = dados.get('nome', usuario['nome'])
            usuario['email'] = dados.get('email', usuario['email'])
            return jsonify(usuario), 200

    return jsonify({'erro': 'Usuário não encontrado'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def deletar_usuario(user_id):
    """
    Deleta um usuário pelo ID.
    ---
    tags:
      - Usuários
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID do usuário
    responses:
      200:
        description: Usuário excluído com sucesso
        schema:
          type: object
          properties:
            mensagem:
              type: string
              example: Usuário excluído com sucesso
      404:
        description: Usuário não encontrado
        schema:
          type: object
          properties:
            erro:
              type: string
              example: Usuário não encontrado
    """
    for usuario in usuarios:
        if usuario['id'] == user_id:
            usuarios.remove(usuario)
            return jsonify({'mensagem': 'Usuário excluído com sucesso'}), 200

    return jsonify({'erro': 'Usuário não encontrado'}), 404

@app.route('/')
def home():
    """
    Página inicial da API.
    ---
    tags:
      - Home
    responses:
      200:
        description: Mensagem de boas-vindas
        schema:
          type: object
          properties:
            mensagem:
              type: string
              example: OLA MUNDO!
    """
    return jsonify({'mensagem': 'OLA MUNDO!'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
