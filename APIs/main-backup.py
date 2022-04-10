from crypt import methods
from os import abort
from flask import Flask, jsonify
from dataclasses import dataclass
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_migrate import Migrate
# import os 
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/flask'
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
CORS(app)

db = SQLAlchemy(app)
# db_path = os.path.realpath(os.path.join(os.path.dirname(__file__), 'app2.db')) engine = create_engine('sqlite://{}'.format(db_path)) 
migrate = Migrate(app, db)


 # this
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
    product_id= db.Column(db.Integer)


    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

@app.route('/api/products')
def index():
    return jsonify(Product.query.all())


@app.route('/api/products/<int:id>/likes', methods=['POST'])
def likes(id):
    req =requests.get('http://localhost:8000/api/user')
    return jsonify(req.json())

    try:
         productuser =  ProductUser(user_id=json['id'], product_id=id)
         db.session,add(productuser)
         db.session.commit()

         publish('product_liked', id)
    except: 
        abort(400,'you already liked')
    return jsonify({
        'message':'success'
    })
          


if __name__ == '__main__' :
    app.run(debug=True, host='127.0.0.1')
