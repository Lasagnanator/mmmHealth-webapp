import hashlib
import werkzeug
import app

#restituisce l'hash di una stringa
def hash512(string):
    hashed=  hashlib.sha512( str( string ).encode("utf-8") ).hexdigest()
    return hashed

