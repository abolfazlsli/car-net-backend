from extensions import db

class Cars (db.Model):
    __bind_key__ = "cars"
    def __init__(self , ownerid , name, carid , model, brandid , title , description , price , images_dir , imagecover , status , expire_date , views , created_at , updated_at):
        self.ownerid = ownerid
        self.name = name
        self.carid = carid
        self.model = model
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
    ownerid = db.Column(db.String , nullable = False)
    name = db.Column(db.String , nullable = False)
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
    model = db.Column(db.String , nullable = False)


class Brands (db.Model):
    __bind_key__ = "cars"
    def __init__(self , brandname , brandid):
        self.brandname = brandname
        self.brandid = brandid
    id = db.Column(db.Integer , primary_key = True)
    brandid = db.Column(db.String , nullable = False , unique = True)
    brandname = db.Column(db.String , nullable = False)

class BrandFeilds (db.Model):
    __bind_key__ = "cars"
    def __init__(self , brandid , fieldtype , fieldname , options , fieldlabel):
        self.brandid = brandid
        self.fieldtype = fieldtype
        self.fieldname = fieldname
        self.options = options
        self.fieldlabel = fieldlabel
    id = db.Column(db.Integer , primary_key = True)
    brandid = db.Column(db.String , nullable = False)
    fieldtype = db.Column(db.String , nullable = False)
    fieldname = db.Column(db.String , nullable = False)
    options = db.Column(db.String , nullable = False)
    fieldlabel = db.Column(db.String , nullable = False)

class FullFeilds (db.Model):
    __bind_key__ = "cars"
    def __init__(self , carid , fieldtype , fieldname , fieldvalue , fieldlabel):
        self.carid = carid
        self.fieldtype = fieldtype
        self.fieldname = fieldname
        self.fieldvalue = fieldvalue
        self.fieldlabel = fieldlabel
    id = db.Column(db.Integer , primary_key = True)
    carid = db.Column(db.String , nullable = False)
    fieldtype = db.Column(db.String , nullable = False)
    fieldname = db.Column(db.String , nullable = False)
    fieldvalue = db.Column(db.String , nullable = False)
    fieldlabel = db.Column(db.String , nullable = False)
