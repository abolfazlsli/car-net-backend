from flask import *
from flask_cors import *
from database import *

#subapps
from admins.admins import admins
from cars.routes import cars as car_bp
from shops.routes import shops
from tokens.routes import tokens
from users.route import users

from extensions import db
from config import SQLALCHEMY_DATABASE_URI , SQLALCHEMY_BINDS
from apiseting import api_seciurety
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS
app.config['CORS_HEADERS'] = 'Content-Type'



app.register_blueprint(admins)
app.register_blueprint(car_bp)
app.register_blueprint(tokens)
app.register_blueprint(shops)
app.register_blueprint(users)

@app.post("/")
def homeurl():
    # api_seciurety.checkapikey(request)
    return{
        "data" : "welcom to home"
    }



@app.errorhandler(Exception)
def Errors(e):
    print(e)
    if e.code == 405:
        return {
            "error" : "method not allowd"
        } , e.code
    elif e.code == 404:
        return {
            "error" : "page not found"
        } , e.code
    elif e.code == 403:
        return {
            "error" : "permision error"
        }
    elif e.code == 500 :
        return {
            "error": "system error"
        } , e.code
    elif e.code == 204:
        return {
            "error": "fill all the blancks "
        } , e.code


db.init_app(app)
app.app_context().push()


db.create_all()



app.run(debug=True)
