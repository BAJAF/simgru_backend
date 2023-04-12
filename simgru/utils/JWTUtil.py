import jwt

secret = "J3kI3hs3407H527"
algorithm = "HS256"

def encodeToken(token: str):
    encoded = jwt.encode({
        "id" : token
    }, secret, algorithm="HS256")

    return encoded

def decodeToken(jwt):
    decode = jwt.decode(jwt, secret, algorithm="HS256")

    return decode