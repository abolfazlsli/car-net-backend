from extensions import db

class Tokens(db.Model):
    __bind_key__ = "tokens"
    def __init__(self , key , user , end_session_time , create_time):
        self.key = key
        self.user = user
        self.end_session_time = end_session_time
        self.create_time = create_time
    id = db.Column(db.Integer , primary_key = True)
    key = db.Column(db.String , unique = True , nullable = False)
    user = db.Column(db.String , nullable = False)
    end_session_time = db.Column(db.Date , nullable=False)
    create_time = db.Column(db.Date , nullable=False)