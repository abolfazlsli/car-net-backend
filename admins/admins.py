from flask import *
from admins.admins_module import *
from apiseting.api_seciurety import checksubapp , checkapikey
from cars.cars_module import Brands , BrandFeilds
from appfunctions import generate_random_string




admins = Blueprint(name="admins" , import_name=__name__ , url_prefix="/admins")


@admins.post("/")
def adminshome () :
    print(request)
    checksubapp("admins")
    checkapikey(request)
    return {
        "data" : "welcom to admins"
    }


@admins.post("/addbrand")
def addbrand () :
    checksubapp("admins")
    # checkapikey(request)
    data = request.json
    print(data)
    brandname = data.get("brandname")
    feilds = data.get("feilds")
    brandid = generate_random_string()
    for i in feilds:
        brandfeild = BrandFeilds(brandid , i.get("feildtype") , i.get("feildname") , str(i.get("options")) , i.get("fieldlabel"))
        db.session.add(brandfeild)
    brand = Brands(brandname , brandid)
    db.session.add(brand)
    db.session.commit()
    return {
        "data" : "brand added successfully"
    }

@admins.get("/getbrands")
def getbrands () :
    checksubapp("admins")
    brands = Brands.query.all()
    return {
        "data" : brands
    }

@admins.put("/updatebrand")
def updatebrand () :
    checksubapp("admins")
    data = request.json
    brandid = data.get("brandid")
    brandname = data.get("brandname")
    brand = Brands.query.filter_by(brandid = brandid).first()
    brand.brandname = brandname
    db.session.commit()
    return {
        "data" : "brand updated successfully"
    }


@admins.delete("/deletebrand")
def deletebrand () :
    checksubapp("admins")
    data = request.json
    brandid = data.get("brandid")
    brand = Brands.query.filter_by(brandid = brandid).first()
    db.session.delete(brand)
    db.session.commit()
    return {
        "data" : "brand deleted successfully"
    }

@admins.get("/")
def adminshomeasget () :
    checksubapp("admins")
    return {
        "data" : "welcom to admins"
    }

