# wsgi.py
import logging
from flask import Flask
from config import Config


try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass # Heroku does not use .env

app = Flask(__name__)
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow # Order is important here!
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import Product
from schemas import products_schema, product_schema

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products')
def products():
    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return products_schema.jsonify(products)


@app.route('/api/v1/products/<int:product_id>')
def product(product_id: int):
    product = db.session.query(Product).get(product_id) # SQLAlchemy request => 'SELECT * FROM products'
    return product_schema.jsonify(product)
