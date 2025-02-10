from extensions import db



class Shop(db.Model):
    __bind_key__ = "shops"
    def __init__(self , digitid , name , password , address , phone , profilepic , bio , banner , dirtoken ):
        self.digitid = digitid
        self.name = name
        self.password = password
        self.address = address
        self.phone = phone
        self.profilepic = profilepic
        self.bio = bio 
        self.banner = banner
        self.dirtoken = dirtoken
    id = db.Column(db.Integer , primary_key = True)
    digitid = db.Column(db.String , unique = True , nullable = False)
    name = db.Column(db.String , nullable = False)
    password = db.Column(db.String , nullable = False)
    address = db.Column(db.String , nullable = True)
    phone = db.Column(db.String , nullable = False , unique = True)
    profilepic = db.Column(db.String , nullable = True)
    bio = db.Column(db.String , nullable = True)
    banner = db.Column(db.String, nullable = False)
    dirtoken = db.Column(db.String , unique=True , nullable = False)