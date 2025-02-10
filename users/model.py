from extensions import db

class Users (db.Model) :
    __bind_key__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=True , unique = True)
    password = db.Column(db.String(128), nullable=False)
    digitalid = db.Column(db.String(50), unique=True, nullable=False)
    profileurl = db.Column(db.String(200), nullable=True)
    assetsdir = db.Column(db.String(200), nullable=True)

    def __init__(self, username, name, lastname, phone, password, digitalid, profileurl, assetsdir):
        self.username = username
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.password = password
        self.digitalid = digitalid
        self.profileurl = profileurl
        self.assetsdir = assetsdir
        

