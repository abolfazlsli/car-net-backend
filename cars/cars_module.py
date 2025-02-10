from extensions import db

class Cars (db.Model):
    __bind_key__ = "cars"
    def __init__(self , name):
        self.name = name
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String)
