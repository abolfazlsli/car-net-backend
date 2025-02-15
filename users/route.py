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
    username = f"user-{phone}"
    digitalid = generate_random_string()
    token_digiid = generate_random_string()
    userdir = f"./users/assets/{username}_{digitalid}"
    try:
        user = Users(username , name , lastname , phone , password , digitalid ,userdir ,userdir)
        token = Tokens(token_digiid , digitalid , set30daysnext() , sendtoday() , request.headers.get('User-Agent')  , "P")
        db.session.add(token)
        db.session.add(user)
        db.session.commit()
        os.mkdir(userdir)
        return {
        "apidata" : {
            'token' : token_digiid ,
            "name" : name
        }
    } , 200
    except :
        return {
            "error" : "repuser"
        } , 500

@users.post("/login")
def loginuser ():
    user = Users.query.filter_by(phone = request.form.get("phone") , password = request.form.get("password"))
    if user.count() > 0:
        token_key = generate_random_string()
        user_key = user.first().digitalid
        token = Tokens(token_key , user_key , set30daysnext() ,sendtoday() , request.headers.get('User-Agent')  , "C")
        db.session.add(token)
        db.session.commit()
        return {
            "token" : token_key ,
            "name" : user.first().name
        } , 200
    return {
        "error" : "invalid user"
    } , 500 
