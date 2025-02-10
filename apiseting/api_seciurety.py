from flask import abort
from dotenv import load_dotenv
import os
from apiseting.config import api_status
load_dotenv()

apikey = os.getenv("API_KEY")

def checkapikey(rq):
    if not rq.form.get("apikey") :
         print("in err" , rq)
         print(apikey)
         abort(403)


def checksubapp (appname) : 
     if not appname in api_status['valid_subapps'] :
          abort(403)