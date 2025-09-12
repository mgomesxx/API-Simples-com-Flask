from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = []
current_id = 1

@app.route('/users', methods=['POST'])
def criar_usuario():
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
    return jsonify(usuarios), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def buscar_usuario_por_id(user_id):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            return jsonify(usuario), 200
    return jsonify({'erro': 'Usuário não encontrado'}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def atualizar_usuario(user_id):
    dados = request.json

    for usuario in usuarios:
        if usuario['id'] == user_id:
            usuario['nome'] = dados.get('nome', usuario['nome'])
            usuario['email'] = dados.get('email', usuario['email'])
            return jsonify(usuario), 200

    return jsonify({'erro': 'Usuário não encontrado'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def deletar_usuario(user_id):
    for usuario in usuarios:
        if usuario['id'] == user_id:
            usuarios.remove(usuario)
            return jsonify({'mensagem': 'Usuário excluído com sucesso'}), 200

    return jsonify({'erro': 'Usuário não encontrado'}), 404

@app.route('/')
def home():
    return jsonify({'mensagem': 'OLA MUNDO!'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)


