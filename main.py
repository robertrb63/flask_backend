from fastapi import FastAPI

from routers import products, users

app=FastAPI()

app.include_router(products.app)
app.include_router(users.app)
 
      
@app.get("/")
async def root():
    return {"url":"http://robert"}
