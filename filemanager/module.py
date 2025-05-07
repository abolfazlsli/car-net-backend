from extensions import db

class File (db.Model):
    __bind_key__ = "files"
    def __init__(self , filename , digitalName , format):
        self.filename = filename
        self.digitalName = digitalName
        self.format = format
    id = db.Column(db.Integer , primary_key = True)
    filename = db.Column(db.String , nullable = False)
    digitalName = db.Column(db.String , unique = True , nullable = False)

