from tokens.module import *
from flask import  *


tokens = Blueprint("tokens" , import_name=__name__ , url_prefix="/tokens")




@tokens.post("/check")
def checktoken () :
    data = request.json
    tok = Tokens.query.filter_by(key = data.get('token'))
    if tok.count() > 0:
        return {
            "data" : "exist"
        } , 200
    else:
        return {
            "data" : "not exist"
        } , 404
@tokens.get("/")
def tokensstart():
    return {
        "data" : "welocm to tokens"
    }
