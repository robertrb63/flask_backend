from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

app=APIRouter(prefix="/products", tags=["products"] ,responses={404:{"message":"No tenemos el producto"}})

class Product(BaseModel):
    id:int
    name:str
    surname:str
    url:str
    age:int

products_list = [Product(id=1, name="Tomate", surname="Restrepo", url="http://rr",age=24),
              Product(id=2, name="Cebolla", surname="Marin", url="http://rr",age=18),
              Product(id=3, name="GArbanzo", surname="Angulo", url="http://rr",age=34),
              Product(id=5, name="Pollos", surname="Martinez", url="http://rr",age=44)]    
       

@app.get("/")
async def products():
    return products_list

@app.get("/{id}")
async def products(id:int):
    products=filter(lambda product:product.id == id, products_list)
    try:
        return list(products)[0]
    except:
        return{"error":"No se encuentra el Usuario"}

@app.post("/product/", status_code=201)  
async def product(product:Product):
    if type(search_product(product.id))==Product:
        raise HTTPException(status_code=204, detail="El Ususario ya existe")   
    products_list.append(product)
    return product  

@app.put("/product/")
async def product(product:Product):
    found = False
    
    for index, saved_product in enumerate(products_list):
        if saved_product.id == product.id:
            products_list[index] = product
            found = True
    if not found:
        return {"error":"No se ha actualizado el Usuario"}
            
@app.delete("/{id}")
async def product(id:int):
    
    found = False
    
    for index, saved_product in enumerate(products_list):
        if saved_product.id == id:
            del products_list[index]
            found = True
    if not found:
        return {"error":"El Usuario no existe"}
    
def search_product(id:int):
    products=filter(lambda product:product.id == id, products_list)
    try:
        return list(products)[0]
    except:
        return{"error":"No se encuentra el Usuario"}  

@app.get("/search_products/{name}")
async def products(name:str):
    procucts=filter(lambda procuct:procuct.id == id, products_list)
    try:
        return list(products)[0]
    except:
        return{"error":"No se encuentra el Usuario con este nombre"}    


 