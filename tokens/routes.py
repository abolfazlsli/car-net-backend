from tokens.module import *
from flask import  *


tokens = Blueprint("tokens" , import_name=__name__ , url_prefix="/tokens")


@tokens.get("/")
def tokensstart():
    return {
        "data" : "welocm to tokens"
    }
