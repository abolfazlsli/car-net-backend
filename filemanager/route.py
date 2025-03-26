from flask import Blueprint , request , send_file
from filemanager.module import FileManager , db
from appfunctions import generate_random_string , check_path , makeDir , sendtoday , removefile
from sqlalchemy import or_
from tokens.module import Tokens
from shops.module import Shop

filemanager = Blueprint(name="filemanager" , import_name=__name__ , url_prefix="/files")




@filemanager.post("/write/shop")
def writefileforshop () :
    print(request)
    data = request.form
    print(data.get("token"))
    file = request.files
    fileid = generate_random_string()
    diginame = f"{fileid}.{file.get("file").filename.split(".")[-1]}"
    user = Tokens.query.filter_by(key = data.get("token"))
    print(user.first().user)
    filedata = FileManager(file.get("file").filename , user.first().user , fileid , data.get("dicription") ,  file.get("file").filename , diginame , sendtoday())
    try:
        if not check_path(f"./filemanager/files/{user.first().user}"):
            makeDir(f"./filemanager/files/{user.first().user}")
    except :
        pass
    db.session.add(filedata)
    db.session.commit()
    file.get("file").save(f"./filemanager/files/{user.first().user}/{diginame}")
    return {
        "apidata" : "file recved"
    }


@filemanager.post("/delete")
def delfile () :
    print(request.json)
    data = request.json
    user = Tokens.query.filter_by(key = data.get("token"))
    file = FileManager.query.filter_by(senderid = user.first().user , filename = data.get("filename"))
    try:
        assetdir = f"./filemanager/files/{user.first().user}/{file.first().digitaldilename}"
        removefile(assetdir)
        file.delete()
        shop = Shop.query.filter_by(userdigitid = user.first().user)
        if data.get("type") == "banner":
            shop.first().banner = ""
        elif data.get("type") == "profile":
            shop.first().profilepic = ""
        db.session.commit()
        return {
            "apidata" : "deleted"
        } , 200 
    except Exception as e: 
        print(e)
        return { 
            "apidat" : 'error'
        } , 500
@filemanager.post("/edit/shop")
def editpricshop () :
    data = request.form
    filedata = request.files.get("newfile")
    user = Tokens.query.filter_by(key = data.get("token"))
    file = FileManager.query.filter_by(senderid = user.first().user , filename = data.get("oldfile"))
    assetdir = f"./filemanager/files/{user.first().user}/{file.first().digitaldilename}"
    try:
        filedata.save(assetdir)
    except:
        return {
            "apidata" : "error"
        } , 500
    return {
        "apidata" : "done"
    } , 200
@filemanager.post("/write")
def writefile () :
    data = request.json
    file = request.files
    fileid = generate_random_string()
    diginame = f"{fileid}.{file.get("file").content_type}"
    filedata = FileManager(file.get("file").filename , data.get("usekey") , fileid , data.get("dicription") ,  file.get("file").filename , diginame)
    if not check_path(f"./filemanager/files/{fileid}_{data.get("usekey")}"):
        makeDir(f"./filemanager/files/{fileid}_{data.get("usekey")}")
    db.session.add(filedata)
    db.session.commit()
    file.get("file").save(f"./filemanager/files/{fileid}_{data.get("usekey")}/{diginame}")
    return {
        "apidata" : "file recved"
    }

@filemanager.get("/read/<searchparam>")
def readfile (searchparam) :
    file = FileManager.query.filter(
        or_(
            FileManager.filename == searchparam , 
            FileManager.digitaldilename == searchparam , 
            FileManager.title == searchparam
        )
    ).first()
    fileoutput = f"./filemanager/files/{file.senderid}/{file.digitaldilename}"
    return send_file(fileoutput , download_name=file.digitaldilename)


