from flask import Blueprint , request , send_file
from filemanager.module import FileManager , db
from appfunctions import generate_random_string , check_path , makeDir , sendtoday
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

@filemanager.post("/read")
def readfile () :
    data = request.json
    file = FileManager.query.filter(
        or_(
            FileManager.filename == data.get("searchparam") , 
            FileManager.digitaldilename == data.get("searchparam") , 
            FileManager.title == data.get("searchparam")
        )
    ).first()
    fileoutput = f"./filemanager/files/{file.fileid}_{file.usekey}/{file.digitaldilename}"
    return send_file(fileoutput , download_name=file.digitaldilename)


