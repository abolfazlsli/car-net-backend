from flask import Blueprint
from cars.cars_module import *
# from apiseting import api_seciurety as ac

cars = Blueprint(name="cars" , import_name=__name__, url_prefix="/cars")



@cars.post("/")
def carshome():
    return { 
        "data" : 'welcom cars'
    }
