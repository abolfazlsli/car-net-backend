from users.model import *
from tokens.module import Tokens
from flask import *
from appfunctions import generate_random_string , set30daysnext , sendtoday , check_reques
import os
users = Blueprint("users" ,import_name=__name__ , url_prefix="/users")



@users.post("/add")
def adduser () :
    data = request.json
    if not check_reques(request):
        abort(204)
    name = data.get("name")
    lastname = data.get("lastname")
    phone = data.get("phone")
    password = data.get("password")
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
    except Exception as e:
        print(e)
        return {
            "error" : "repuser"
        } , 500

@users.post("/login")
def loginuser ():
    data = request.json
    user = Users.query.filter_by(phone = data.get("phone") , password = data.get("password"))
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
    data = request.json
    tok = Tokens.query.filter_by(key = data.get("token"))
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
    data = request.json
    token = data.get("token")
    name = data.get("name")
    lastname = data.get("lastname")
    phone = data.get("phone")
    username = data.get("username")
    userid = Tokens.query.filter_by(key = token).first().user
    user = Users.query.filter_by(digitalid = userid)
    activity = Activity(user.first().digitalid , "تغییرات" , "done" , generate_random_string())
    user.first().name = name
    user.first().lastname = lastname
    user.first().phone = phone
    user.first().username = username
    db.session.add(activity)
    db.session.commit()
    return "done"
    

@users.post("/check/username")
def checkuser () :
    data = request.json
    username = data.get("username")
    user = Users.query.filter_by(username = username)
    if user.count () > 0 : 
        return {
            "data" : True
        }
    else :
        return {
            "data" : False
        }



@users.post("/send/activiy")
def sendactivys():
    data = request.json
    token = data.get("token")
    userid = Tokens.query.filter_by(key = token)
    useractivty = Activity.query.filter_by(userid = userid.first().user).all()
   
    apidata = [
       {
           "action" : columns.action ,
           "status" : columns.status,
           "date" : columns.date
       } for columns in useractivty
   ]
    return {
        "apidata" : apidata
    }
