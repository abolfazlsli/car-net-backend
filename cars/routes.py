from flask import Blueprint , request
from cars.cars_module import *
from appfunctions import generate_random_string , set30daysnext , sendtoday
import os
# from apiseting import api_seciurety as ac

cars = Blueprint(name="cars" , import_name=__name__, url_prefix="/cars")



@cars.post("/")
def carshome():
    return { 
        "data" : 'welcom cars from dev'
    }


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

@cars.post("/getbrandfilds")
def getbrandfilds():
    data = request.json
    brandid = data.get("brandid")
    fields = BrandFeilds.query.filter_by(brandid=brandid).all()
    return {
        "data" : fields
    }

@cars.post("/addcar")
def addcar():
    data = request.json
    carid = generate_random_string()
    path = f"./cars/assets/{carid}"
    os.makedirs(path)
    images_dir = path
    fields = data.get("fields")
    for i in fields:
        field = FullFeilds(carid, i.get("fieldtype"), i.get("fieldname"), i.get("fieldvalue"), i.get("fieldlabel"))
        db.session.add(field)
    car = Cars(data.get("name"), carid, data.get("model"), data.get("brandid"), data.get("title"), data.get("description"), data.get("price"), images_dir, data.get("imagecover"), "pinding", set30daysnext(), 0, sendtoday(), sendtoday())
    db.session.add(car)
    db.session.commit()
    print(data)
    return {
        "data" : "car added successfully"
    }