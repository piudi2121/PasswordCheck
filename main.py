from fastapi import FastAPI

app = FastAPI()

@app.get('/check/{password}')
def check_password(password: str):
    response = { "validation" : {}, "validated" : True}
    response["validation"]["special_char"] = not password.isalnum()
    response["validation"]["more_than_eight"] = len(password) > 8
    response["validation"]["number"] = hasNumber(password)
    response["validation"]["upper_char"] = hasUpper(password)
    for v in response['validation'].values():
        if v == False:
            response["validated"] = False
            break
    return response


def hasNumber(string: str):
    for char in string:
        if char.isdigit():
            return True
    return False

def hasUpper(string: str):
    for char in string:
        if char.isupper():
            return True
    return False