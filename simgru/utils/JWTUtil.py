import jwt

secret = "J3kI3hs3407H527"
algorithm = "HS256"

def encodeToken(token: str):
    encoded = jwt.encode({
        "token" : token
    }, secret, algorithm="HS256")

    return encoded

def decodeToken(_jwt):
    decode = jwt.decode(_jwt, secret, algorithms=["HS256"])
    return decode