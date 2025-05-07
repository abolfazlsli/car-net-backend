from flask import *
from shops.module import *
from appfunctions import generate_random_string
from tokens.module import *
import os

shops = Blueprint(name="shops" , import_name=__name__, url_prefix="/shops")




@shops.post("/")
def homeshop ():
    return {
        'data' : 'welcom to shop'
    }



@shops.post("/add")
def addShop ():
    data = request.json
    userinformation = Tokens.query.filter_by(key = data.get("token")).first()
    print(userinformation)
    shopdigiid = generate_random_string()
    assetssdir = f"./filemanager/files/{userinformation.user}"
    shop = Shop(userinformation.user , shopdigiid , data.get("name") , data.get("address") , data.get("phone") , data.get("profilepic") , data.get("bio") , data.get("banner") , assetssdir , data.get("shopid"))
    db.session.add(shop)
    db.session.commit()
    return {
        "apidata" : "shop added successfully"
    }



@shops.post("/checkshop") 
def checkshop ():
    data = request.json
    userid = Tokens.query.filter_by(key = data.get("token")).first().user
    if userid == None:
        return {
            "apidata" : "user not found"
        } , 404
    shop = Shop.query.filter_by(userdigitid = userid)
    if shop.count() == 0:
        return {
            "apidata" : "shop not found"
        } , 404
    return {
        "apidata" : "shop found"
    } , 200


@shops.post("/getshop")
def getshop ():
    data = request.json
    user = Tokens.query.filter_by(key = data.get("token"))
    shop = Shop.query.filter_by(userdigitid = user.first().user)
    if not shop.count() == 0:
        apidata = {
            "name" : shop.first().name ,
            "address" : shop.first().address ,
            "phone" : shop.first().phone ,
            "profilepic" : shop.first().profilepic ,
            "bio" : shop.first().bio ,
            "banner" : shop.first().banner ,
        }
    else : 
        apidata = {
            "apidata" : "shop not found"
        }
    return {
        "apidata" : apidata
    }



@shops.post("/editpics")
def editpic () :
    data = request.json
    user = Tokens.query.filter_by(key = data.get("token"))
    shop = Shop.query.filter_by(userdigitid = user.first().user)
    if data.get("type") == "banner" : 
        shop.first().banner = data.get("picname")
    elif data.get("type") == "profile" : 
        shop.first().profilepic = data.get("picname")
    db.session.commit()
    return {
        "apidata" : "pic chnaged" 
    } , 200