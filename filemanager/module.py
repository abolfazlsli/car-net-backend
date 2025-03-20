from extensions import db

class FileManager (db.Model) :
    __bind_key__ = "files"
    def __init__(self , filename, usekey, fileid , dicription , title , digitaldilename , create_at) :
        self.filename = filename
        self.usekey = usekey
        self.fileid = fileid
        self.dicription = dicription
        self.title = title
        self.digitaldilename = digitaldilename
        self.create_at = create_at
    id = db.Column(db.Integer , primary_key = True)
    filename = db.Column(db.String , nullable = False)
    usekey = db.Column(db.String , nullable = False)
    fileid = db.Column(db.String , nullable = False , unique = True) # xxx-xxx-xxx-xxx
    dicription = db.Column(db.String , nullable = False)
    title = db.Column(db.String , nullable = False)
    digitaldilename = db.Column(db.String , nullable = False)   # the file name is the real file name that may be persion or unread able type we use this name to save the file and use the file name to read the file 
    create_at = db.Column(db.String , nullable = False)
