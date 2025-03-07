from extensions import db

class Cars (db.Model):
    __bind_key__ = "cars"
    def __init__(self , name):
        self.name = name
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String)



class Brands (db.Model):
    __bind_key__ = "cars"
    def __init__(self , brandname , brandid):
        self.brandname = brandname
        self.brandid = brandid
    id = db.Column(db.Integer , primary_key = True)
    brandid = db.Column(db.String , nullable = False , unique = True)
    brandname = db.Column(db.String , nullable = False)