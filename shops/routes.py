from flask import *
from shops.module import *

shops = Blueprint(name="shops" , import_name=__name__, url_prefix="/shops")




@shops.post("/")
def homeshop ( ):
    return {
        'data' : 'welcom to shop'
    }
