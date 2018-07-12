# wsgi.py
import logging
from flask import Flask, request, jsonify
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

@app.errorhandler(404)
def page_not_found(e):
    response = {
        'url': request.url,
        'status': 404,
        'message': 'not found'
    }
    return jsonify(response), 404

@app.route('/api/v1/products')
def products():
    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return products_schema.jsonify(products)

@app.route('/api/v1/products/<int:product_id>', methods=['GET'])
def product(product_id: int):
    product = db.session.query(Product).get_or_404(product_id) # SQLAlchemy request => 'SELECT * FROM products'
    
    return product_schema.jsonify(product)

@app.route('/api/v1/products/', methods=['POST'])
def create_product():
    requested_object = request.get_json()
    new_object = Product()
    try:
        for attr in ['name', 'description']:
            setattr(new_object, attr, requested_object[attr])
    except KeyError:
        return '', 400

    db.session.add(new_object)
    db.session.commit()

    return product_schema.jsonify(new_object)

@app.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id: int):
    product = db.session.query(Product).get_or_404(product_id) # SQLAlchemy request => 'SELECT * FROM products'
    
    db.session.delete(product) # SQLAlchemy request => 'SELECT * FROM products'
    db.session.commit()

    return '', 204

@app.route('/api/v1/products/<int:product_id>', methods=['PATCH'])
def update_product(product_id: int):
    product = db.session.query(Product).get_or_404(product_id) # SQLAlchemy request => 'SELECT * FROM products'

    try:
        for attr in ['name', 'description']:
            setattr(product, attr, request.get_json()[attr])
    except KeyError:
        pass

    db.session.commit()

    return product_schema.jsonify(product)