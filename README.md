# BookTrack – Gerenciador de Leitura

Projeto simples desenvolvido com **Django + Python + HTML + CSS puro**, com o objetivo de registrar e acompanhar os livros que o usuário está lendo, pretende ler ou já leu.

## Funcionalidades

- Listagem de livros com status de leitura
- Cadastro de novos livros
- Interface limpa e responsiva com CSS puro
- Estrutura organizada por componentes

## Tecnologias

- Python 3
- Django 5.x
- HTML5
- CSS3
- SQLite (banco de dados embutido)

## Instalação

```bash
git clone https://github.com/seu-usuario/booktrack-django.git
cd booktrack-django
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
