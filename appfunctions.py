import random ,string, os
from datetime import datetime, timedelta , date
from http.cookies import SimpleCookie

def generate_random_string():
    def random_segment(length=4):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    return '-'.join(random_segment() for _ in range(4))




def removefile (name) :
    os.remove(name)


def set30daysnext():
    today = date.today()
    try:
        date_obj = datetime.combine(today, datetime.min.time())
        
        new_date = date_obj + timedelta(days=30)
        
        return new_date.date()
    except Exception as e:
        print("خطا:", e)
        return None 



def sendtoday ():
    return date.today()




def check_reques (request):
    print(request.form.keys())
    for i in list(request.form.keys()):
        if len(i) == 0 and i == "" :
            return False
    return True


def check_path (path) :
    return os.path.exists(path)



def makeDir (name):
    os.mkdir(name)
    

def getToken(request) : 
    cookie = SimpleCookie()
    cookie.load(request.headers.get("Cookie"))
    token = cookie.get("token").value if cookie.get("token") else None
    return token