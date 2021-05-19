import requests
from dataclasses import dataclass
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint

from producer import publish

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
db = SQLAlchemy(app)
CORS(app)

# models
@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass
class ProductUser(db.Model):
    id: int
    user_id: int
    product_id: str

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

# routes
@app.route('/api/products')
def index():
    return jsonify(Product.query.all())

@app.route('/api/product_users')
def get_product_users():
    return jsonify(ProductUser.query.all())

@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://docker.for.mac.localhost:8000/api/user')
    try:
        user_id = req.json()['id']
        product_user = ProductUser(user_id=user_id, product_id=id)
        db.session.add(product_user)
        db.session.commit()

        # publish event to rabbitmq
        publish('product_liked', id)
    except Exception as e:
        abort(400, str(e))
    return jsonify({
        'message': 'success'
    })
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')