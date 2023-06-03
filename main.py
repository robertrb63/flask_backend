from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    id:int
    name:str
    surname:str
    url:str
    age:int

users_list = [User(id=1, name="Roberto", surname="Restrepo", url="http://rr",age=24),
              User(id=2, name="Rodrigo", surname="Marin", url="http://rr",age=18),
              User(id=3, name="Raul", surname="Angulo", url="http://rr",age=34),
              User(id=5, name="Cesar", surname="Martinez", url="http://rr",age=44)]    
       

@app.get("/")
async def root():
    return {"url":"http://robert"}

@app.get("/users")
async def users():
    return users_list


@app.get("/users/{id}")
async def users(id:int):
    users=filter(lambda user:user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return{"error":"No se encuentra el Usuario"}


@app.post("/user/")  
async def user(user:User):
    if type(search_user(user.id))==User:
        return {"error":"El Ususario ya existe"}
    else:
        users_list.append(user)  


def search_user(id:int):
    users=filter(lambda user:user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return{"error":"No se encuentra el Usuario"}  



@app.get("/search_users/{name}")
async def users(name:str):
    users=filter(lambda user:user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return{"error":"No se encuentra el Usuario con este nombre"}    



    