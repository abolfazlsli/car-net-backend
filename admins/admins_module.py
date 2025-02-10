from extensions import db


class Admins(db.Model):
    __bind_key__ = "admins"
    def __init__(self , digitid , username , name , lastname , acsess_level , phone , password ) : 
        self.digitid = digitid
        self.username = username
        self.phone = phone 
        self.name = name
        self.lastname = lastname
        self.acsess_level = acsess_level
        self.password = password
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String , nullable = False)
    lastname = db.Column(db.String , nullable = True)
    digitid = db.Column(db.String , unique = True , nullable = False)
    username = db.Column(db.String , unique = True , nullable = False)
    acsess_level = db.Column(db.String , unique = False , nullable = False)
    phone = db.Column(db.String , unique = True , nullable = False)
    password = db.Column(db.String)
