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
        activity = Activity(digitalid , "ثبت نام" , "done" , generate_random_string())
        token = Tokens(token_digiid , digitalid , set30daysnext() , sendtoday() , request.headers.get('User-Agent')  , "P")
        db.session.add(token)
        db.session.add(user)
        db.session.add(activity)
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
        activity = Activity(user_key , "ورود" , "done" , generate_random_string())
        db.session.add(token)
        db.session.add(activity)
        db.session.commit()
        return {
            "token" : token_key ,
            "name" : user.first().name
        } , 200
    return {
        "error" : "invalid user"
    } , 500 




@users.post("/me")
def me () :
    data = request.form['token']
    tok = Tokens.query.filter_by(key = data)
    userinfo = Users.query.filter_by(digitalid = tok.first().user)
    apidata = {
        "username" : userinfo.first().username , 
        "name" : userinfo.first().name , 
        "lastname" : userinfo.first().lastname, 
        "phone" : userinfo.first().phone , 
        "profileurl" : userinfo.first().profileurl , 
        "assetsdir" : userinfo.first().assetsdir
    }
    return apidata


@users.post("/edituser") 
def editUser () :
    token = request.form.get("token")
    name = request.form.get("name")
    lastname = request.form.get("lastname")
    phone = request.form.get("phone")
    userid = Tokens.query.filter_by(key = token).first().user
    user = Users().query.filter_by(digitalid = userid)
    

@users.post("/check/username")
def checkuser () :
    data = request.form.get("username")
    user = Users.query.filter_by(username = data)
    if user.count () > 0 : 
        return {
            "data" : True
        }
    else :
        return {
            "data" : False
        }
