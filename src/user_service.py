"""
    User Service
"""
from datetime import datetime, timedelta
# pylint: disable=syntax-error
from jose import jwt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Mock database
users = {"admin": {"password": "admin"}}
SECRET_KEY = "mysecretkey"

class User(BaseModel):
    """
    User(BaseModel)
    :param username
    :param password
    """
    username: str
    password: str

def authenticate_user(username: str, password: str):
    """
    authenticate_user
    :param username:
    :param password:
    :return:
    """
    user = users.get(username)
    if not user or user["password"] != password:
        return False
    return True

@app.post("/login/")
def login(user: User):
    """
    /login/
    :param user:
    :return:
    """
    if not authenticate_user(user.username, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = jwt.encode({"sub": user.username, "exp": datetime.now() + timedelta(hours=1)},
                       SECRET_KEY)
    return {"access_token": token}
