"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi85frhp8u7g2ehp2u0-a.oregon-postgres.render.com",
        database="todo_npiz",
        user="root",
        password="n3kwDJtZVVeJ2MZSvGb0YqobPnekZXd7")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
