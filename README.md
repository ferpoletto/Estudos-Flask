# Estudos-Flask
Repositório referentes aos estudos de Flask.

venv/bin/pip3 install -r requeriments.txt - para instalar as dependencias quando o projeto por clonado

Organização de arquivos > Modelo MVC: controllers, models, static, templates

pastas static e templates = Views do MVC

BANCO DE DADOS
3 tabelas:
User (id, username, password, name, email)
post (id, content, id_user)
follow (id, id_user, id_follower)

Para fazer a comunicação com o banco de dados estarei usando o FlaskSQLAlchemy

venv/bin/pip3 install flask-sqlalchemy