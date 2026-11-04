# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar um catálogo de livros usando o framework FastAPI. Pratique criação de rotas, métodos HTTP, validação de dados com modelos Pydantic e respostas de erro HTTP.

## 📝 Tarefas

### 🛠️ Criar a aplicação e listar livros

#### Descrição

Prepare o ambiente, execute o código inicial e crie as rotas básicas para verificar se a API está ativa e listar os livros disponíveis.

#### Requisitos

O programa concluído deve:

- Instalar FastAPI e Uvicorn com `python -m pip install fastapi uvicorn`.
- Executar a aplicação com `python starter-code.py`.
- Retornar uma mensagem de confirmação na rota `GET /`.
- Retornar todos os livros cadastrados na rota `GET /books`.
- Permitir explorar e testar as rotas pela documentação interativa em `/docs`.

### 🛠️ Consultar e cadastrar livros

#### Descrição

Adicione operações para consultar um livro pelo identificador e cadastrar novos livros. Use os modelos Pydantic do código inicial para validar os dados enviados.

#### Requisitos

O programa concluído deve:

- Retornar um livro específico na rota `GET /books/{book_id}`.
- Responder com status HTTP `404` quando o identificador não existir.
- Cadastrar livros pela rota `POST /books`, gerando um identificador único.
- Validar os campos `title` e `author` recebidos no cadastro.
- Responder com status HTTP `201` após cadastrar um livro.

### 🛠️ Atualizar e remover livros

#### Descrição

Complete as operações de gerenciamento implementando a atualização e a remoção de livros existentes.

#### Requisitos

O programa concluído deve:

- Atualizar um livro pela rota `PUT /books/{book_id}`.
- Remover um livro pela rota `DELETE /books/{book_id}`.
- Retornar status HTTP `404` ao tentar atualizar ou remover um identificador inexistente.
- Usar status HTTP apropriados para as operações concluídas.
- Confirmar na rota `GET /books` que as alterações e remoções foram aplicadas.
