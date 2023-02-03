import hashlib

def hash512(string):
    hashed=  hashlib.sha512( str( string ).encode("utf-8") ).hexdigest()
    return hashed

def passwdcheck():
    if 

    check = False  
    return check