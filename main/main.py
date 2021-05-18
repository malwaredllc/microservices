import requests
from dataclasses import dataclass
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import UniqueConstraint

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
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

# routes
@app.route('/api/products')
def index():
    return jsonify(Product.query.all())

@app.route('/api/products<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get('http://localhost:8000/api/user')
    return req.json()
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')