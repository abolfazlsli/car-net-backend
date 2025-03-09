from extensions import db

class Cars (db.Model):
    __bind_key__ = "cars"
    def __init__(self , name, carid , brandid , title , description , price , images_dir , imagecover , status , expire_date , views , created_at , updated_at):
        self.name = name
        self.carid = carid
        self.brandid = brandid
        self.title = title
        self.description = description
        self.price = price
        self.images_dir = images_dir
        self.imagecover = imagecover
        self.status = status # pinding , active , inactive , deleted , archive , blocked , expired
        self.expire_date = expire_date
        self.views = views
        self.created_at = created_at
        self.updated_at = updated_at
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String)
    carid = db.Column(db.String , nullable = False , unique = True)
    brandid = db.Column(db.String , nullable = False)
    title = db.Column(db.String , nullable = False)
    description = db.Column(db.String)
    price = db.Column(db.String , nullable = False)
    images_dir = db.Column(db.String , nullable = False)
    imagecover = db.Column(db.String , nullable = False)
    status = db.Column(db.String , nullable = False)
    expire_date = db.Column(db.String , nullable = False)
    views = db.Column(db.Integer , nullable = False)
    created_at = db.Column(db.String , nullable = False)
    updated_at = db.Column(db.String , nullable = False)


class Brands (db.Model):
    __bind_key__ = "cars"
    def __init__(self , brandname , brandid):
        self.brandname = brandname
        self.brandid = brandid
    id = db.Column(db.Integer , primary_key = True)
    brandid = db.Column(db.String , nullable = False , unique = True)
    brandname = db.Column(db.String , nullable = False)

class BrandFiles (db.Model):
    __bind_key__ = "cars"
    def __init__(self , brandid , filetype , filename):
        self.brandid = brandid
        self.filetype = filetype
        self.filename = filename
    id = db.Column(db.Integer , primary_key = True)
    brandid = db.Column(db.String , nullable = False)
    filetype = db.Column(db.String , nullable = False)
    filename = db.Column(db.String , nullable = False)
    options = db.Column(db.String , nullable = False)

class FullFiles (db.Model):
    __bind_key__ = "cars"
    def __init__(self , carid , filetype , filename , fileidvalue):
        self.carid = carid
        self.filetype = filetype
        self.filename = filename
        self.fileidvalue = fileidvalue
    id = db.Column(db.Integer , primary_key = True)
    carid = db.Column(db.String , nullable = False)
    filetype = db.Column(db.String , nullable = False)
    filename = db.Column(db.String , nullable = False)
    fileidvalue = db.Column(db.String , nullable = False)
