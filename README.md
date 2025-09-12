# API-Simples-com-Flask

 __Disciplina:__ Desenvolvimento de APIs e Microserviços.
 
 __Integrantes:__ Ana Carolina Guedes, Maria Eduarda Gomes e Suzana Kelly Guedes

 __Grupo:__ 9

---

__Descrição do Projeto__

Este projeto consiste na construção de uma aplicação web simples utilizando o framework Flask para criar uma API RESTful que gerencia usuários.

A API implementa as quatro operações fundamentais de CRUD (Create, Read, Update, Delete) para o recurso usuário.

Os dados dos usuários são armazenados temporariamente em uma estrutura de dados em memória (como uma lista de dicionários), simulando um banco de dados simples.


# Rota para CRIAR um novo usuário (POST /users)
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
              example: "Digite seu nome"
    """

# Rota para LISTAR todos os usuários (GET /users)
@app.route('/users', methods=['GET'])
def listar_usuarios():
    """
    Lista todos os usuários.
    ---
    tags:
      - Usuários
    produces:
      - application/json
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

# Rota para BUSCAR um usuário por ID (GET /users/{user_id})
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
        description: ID do usuário a ser buscado
        required: true
        type: integer
        example: 1
    produces:
      - application/json
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

