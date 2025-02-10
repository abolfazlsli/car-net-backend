from flask import *
from flask_cors import *
from database import *
from admins.admins import admins
from cars.routes import cars as car_bp
from shops.routes import shops
from tokens.routes import tokens
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

@app.post("/")
def homeurl():
    # api_seciurety.checkapikey(request)
    return{
        "data" : "welcom to home"
    }



@app.errorhandler(Exception)
def Errors(e):
    if e.code == 405:
        return {
            "error" : "method not allowd"
        } , e.code
    if e.code == 404:
        return {
            "error" : "page not found"
        } , e.code
    if e.code == 403:
        return {
            "error" : "permision error"
        }


db.init_app(app)
app.app_context().push()


db.create_all()



app.run(debug=True)
