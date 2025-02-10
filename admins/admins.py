from flask import *
from admins.admins_module import *
from apiseting.api_seciurety import checksubapp , checkapikey
admins = Blueprint(name="admins" , import_name=__name__ , url_prefix="/admins")


@admins.post("/")
def adminshome () :
    print(request)
    checksubapp("admins")
    checkapikey(request)
    return {
        "data" : "welcom to admins"
    }

@admins.get("/")
def adminshomeasget () :
    checksubapp("admins")
    return {
        "data" : "welcom to admins"
    }

