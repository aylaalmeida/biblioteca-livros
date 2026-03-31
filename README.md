Biblioteca de Livros

Descrição

Este projeto consiste em uma API REST desenvolvida com Django para o gerenciamento de livros, permitindo cadastrar, visualizar e filtrar livros por status.

Objetivo

Aplicar conceitos de desenvolvimento back-end utilizando Django, criação de APIs REST e versionamento com Git e GitHub.

Funcionalidades

- Cadastrar livros
- Listar todos os livros
- Filtrar livros por status (Lido, Lendo, Quero Ler)
- Visualizar informações dos livros

Estrutura de Dados

Cada livro possui os seguintes campos:

- Título
- Autor
- Descrição
- Status (LIDO, LENDO, QUERO_LER)

Rotas da API

Listar todos os livros:
GET /api/livros/

Filtrar livros que estão sendo lidos:
GET /api/livros/lendo/

Tecnologias utilizadas

- Python
- Django
- Django REST Framework
- SQLite
- Git e GitHub

Como executar o projeto

1. Clonar o repositório:
   git clone https://github.com/aylaalmeida/biblioteca-livros.git

2. Acessar a pasta:
   cd backend

3. Criar ambiente virtual:
   python -m venv venv

4. Ativar o ambiente:
   venv\Scripts\activate

5. Instalar dependências:
   pip install -r requirements.txt

6. Rodar migrações:
   python manage.py migrate

7. Iniciar servidor:
   python manage.py runserver
