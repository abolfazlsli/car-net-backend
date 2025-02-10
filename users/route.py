from users.model import *
from tokens.module import Tokens
from flask import *
from appfunctions import generate_random_string , set30daysnext , sendtoday , check_reques
import os
users = Blueprint("users" ,import_name=__name__ , url_prefix="/users")



@users.post("/add")
def adduser () :
    if not check_reques(request):
        abort(204)
    name = request.form.get("name")
    lastname = request.form.get("lastname")
    phone = request.form.get("phone")
    password = request.form.get("password")
    username = f"user{phone}"
    digitalid = generate_random_string()
    token_digiid = generate_random_string()
    userdir = f"./assets/{username}_{digitalid}"
    os.mkdir(userdir)
    user = Users(username , name , lastname , phone , password , digitalid ,userdir)
    token = Tokens(token_digiid , digitalid , set30daysnext() , sendtoday() , request.headers.get('User-Agent')  , "P")
    db.session.add(token)
    db.session.add(user)
    db.session.commit()
    return {
        "apidata" : {
            'token' : token_digiid
        }
    } , 200
@users.post("/login")
def loginuser ():
    return {
        "data" : 'here'
    }
