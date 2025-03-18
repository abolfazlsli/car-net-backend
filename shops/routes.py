from flask import *
from shops.module import *
from appfunctions import generate_random_string


shops = Blueprint(name="shops" , import_name=__name__, url_prefix="/shops")




@shops.post("/")
def homeshop ( ):
    return {
        'data' : 'welcom to shop'
    }


@shops.post("/add")
def addShop ():
    data = request.json
    digiid = generate_random_string()
    shop = Shop(digiid , data.get("shopname") , "" , data.get("address") , data.get("phone") , data.get("profilepic") , data.get("bio") , data.get("banner") , data.get("dirtoken")) 
    # adding connectionid to user and shop to database filds
    return {
        "apidata" : ""
    }
