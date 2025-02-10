from extensions import db



class Users(db.Model):
    def __init__(self , digitid , phone , username , name , lastname , password ):
        self.digiid = digitid
        self.phone = phone
        self.username = username
        self.name = name
        self.lastname = lastname
        self.password = password
    id = db.Column(db.Integer , primary_key = True)
    digiid = db.Column(db.String , unique = True , nullable = False)
    phone = db.Column(db.String , unique = True , nullable = False)
    name = db.Column(db.String , nullable = False)
    lastname = db.Column(db.String , nullable = True)
    password = db.Column(db.String , nullable = False)
        

