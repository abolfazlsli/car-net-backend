from flask import Blueprint , request
import json
from cars.cars_module import * 
from tokens.module import Tokens
from appfunctions import generate_random_string , set30daysnext , sendtoday , getToken

import os
# from apiseting import api_seciurety as ac

cars = Blueprint(name="cars" , import_name=__name__, url_prefix="/cars")



@cars.post("/")
def carshome():
    return { 
        "data" : 'welcom cars from dev'
    }


@cars.post("/my-cars")
def getAllCars () :
    # print(request.headers)
    tok = getToken(request)
    print(tok)
    offsetFrom = request.json.get("from")
    offsetTo = request.json.get("to")
    owner = Tokens.query.filter_by(key=tok)
    cars = Cars.query.filter_by(ownerid = owner.first().user).all()
    total = len(cars)
    data = cars[int(offsetFrom):int(offsetTo)]
    apidata = [
        {
            "name" : i.name ,
            "title" : i.title ,
            "images" : i.images_dir ,
            "cover" : json.loads(i.images_dir) ,
            "filds" : [
                {
                    "fieldtype" : field.fieldtype ,
                    "fieldvalue" : field.fieldvalue ,
                    "fieldlabel" : field.fieldlabel
                }
                for field in FullFeilds.query.filter_by(carid = i.carid).all()
                ]
        }
        for i in data 
    ]
    return {"apidata" : apidata , "total" : total}
@cars.get("/brands")
def get_all_models():
    models = Brands.query.all()
    apidata = [{
        "label" : i.brandname ,
        "value" : i.brandid 
    } for i in models]
    return {
        "apidata" : apidata
    }


@cars.get("/getfields")
def getfields():
    fields = FullFeilds.query.all()
    return {
        "data" : fields
    }


@cars.get("/fixdata")
def fix () :
    data = BrandFeilds.query.all()
    for i in data:
        i.options = i.options.replace("'" , '"')
    db.session.commit()
    return "done"

@cars.post("/getbrandfilds")
def getbrandfilds():
    data = request.json
    brandid = data.get("brandid")
    fields = BrandFeilds.query.filter_by(brandid=brandid).all()
    apidata = [{
        "fieldname" : filde.fieldname , 
        "fieldtype" : filde.fieldtype ,
        "options" : json.loads(filde.options) ,
        "fieldlabel" : filde.fieldlabel
    } for filde in fields ]
    print(apidata)
    return {
        "data" : apidata
    }

@cars.post("/addcar")
def addcar():
    data = request.json
    print(data.get("datas"))
    carid = generate_random_string()
    user = Tokens.query.filter_by(key = data.get("token"))
    path = f"./filemanager/files/{user.first().user}/cars/{carid}"
    carbrand = Brands.query.filter_by(brandid = data.get("brandid"))
    carname = carbrand.first().brandname
    images_dir = data.get("images")
    fields = data.get("datas")
    for i in fields:
        field = FullFeilds(carid, i.get("fieldtype"), i.get("fieldname"), i.get("fieldvalue"), i.get("fieldlabel"))
        db.session.add(field)
    car = Cars(user.first().user , carname, carid, data.get("model"), data.get("brandid"), data.get("title"), data.get("description"), data.get("price"), json.dumps(images_dir), data.get("imagecover"), "pinding", set30daysnext(), 0, sendtoday(), sendtoday() )
    db.session.add(car)
    db.session.commit()
    print(data)
    return {
        "data" : "car added successfully" ,
        "carid" : carid
    }

