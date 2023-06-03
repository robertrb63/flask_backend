from fastapi import FastAPI, HTTPException
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

@app.post("/user/", status_code=201)  
async def user(user:User):
    if type(search_user(user.id))==User:
        raise HTTPException(status_code=204, detail="El Ususario ya existe")   
    users_list.append(user)
    return user  

@app.put("/user/")
async def user(user:User):
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error":"No se ha actualizado el Usuario"}
            
@app.delete("/user/{id}")
async def user(id:int):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error":"El Usuario no existe"}
    
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


 
