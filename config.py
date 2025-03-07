SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
SQLALCHEMY_BINDS  = {
    "admins" : "sqlite:///admins.db" , 
    "cars" : "sqlite:///cars.db",
    "tokens" : "sqlite:///tokens.db" , 
    "shops" : 'sqlite:///shops.db' , 
    'users' : 'sqlite:///users.db' , 
    "models" : "sqlite:///filters.db"
} 
SQLALCHEMY_TRACK_MODIFICATIONS = False