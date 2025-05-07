from flask import Blueprint , request , send_file , send_from_directory
from filemanager.module import File, db

from appfunctions import generate_random_string , check_path , makeDir , sendtoday , removefile , getToken
from sqlalchemy import or_ , and_
from tokens.module import Tokens
from shops.module import Shop
from http.cookies import SimpleCookie
import os

filemanager = Blueprint(name="filemanager" , import_name=__name__ , url_prefix="/files" , static_folder="files")








#uploader 
@filemanager.post("/")
def upload () :
    file = request.files
    filedata = file.get("file").filename.split(".")[-1] in ["jpg" , "png" , "jpge"] or None
    if not filedata :  return {"apidata" : "file not valid most be ( jpg , png , jpge )"} , 400
    digitalName = generate_random_string()
    file.get("file").save(f"./filemanager/files/{digitalName}.{file.get("file").filename.split(".")[-1]}")
    db.session.add(File(file.get("file").filename , digitalName , file.get("file").filename.split(".")[-1]))
    db.session.commit()
    return {
        "apidata" : "file saved" ,
        "digitalname":f"{digitalName}.{file.get("file").filename.split(".")[-1]}"
    } , 200


# delete file
@filemanager.delete("/")
def delete():
    return {
        "apidata" : "deleted"
    }


# read file

@filemanager.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(os.path.join(filemanager.root_path, 'files'), filename)

