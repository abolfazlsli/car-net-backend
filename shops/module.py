from extensions import db



class Shop(db.Model):
    __bind_key__ = "shops"
    def __init__(self , userdigitid , digitid , name , address , phone , profilepic , bio , banner , assetssdir , shopid ):
        self.userdigitid = userdigitid
        self.digitid = digitid
        self.name = name
        self.address = address
        self.phone = phone
        self.profilepic = profilepic
        self.bio = bio 
        self.banner = banner
        self.assetssdir = assetssdir
        self.shopid = shopid
    id = db.Column(db.Integer , primary_key = True)
    userdigitid = db.Column(db.String , nullable = False)
    digitid = db.Column(db.String , unique = True , nullable = False)
    name = db.Column(db.String , nullable = False , unique = True)
    address = db.Column(db.String , nullable = True)
    phone = db.Column(db.String , nullable = False , unique = True)
    profilepic = db.Column(db.String , nullable = True)
    bio = db.Column(db.String , nullable = True)
    banner = db.Column(db.String, nullable = False)
    assetssdir = db.Column(db.String , nullable = False)
    shopid = db.Column(db.String , unique = True )