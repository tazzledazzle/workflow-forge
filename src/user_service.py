from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta

app = FastAPI()

# Mock database
users = {"admin": {"password": "admin"}}
SECRET_KEY = "mysecretkey"

class User(BaseModel):
    username: str
    password: str

def authenticate_user(username: str, password: str):
    user = users.get(username)
    if not user or user["password"] != password:
        return False
    return True

@app.post("/login/")
def login(user: User):
    if not authenticate_user(user.username, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = jwt.encode({"sub": user.username, "exp": datetime.utcnow() + timedelta(hours=1)}, SECRET_KEY)
    return {"access_token": token}
