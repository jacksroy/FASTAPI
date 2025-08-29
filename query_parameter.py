from fastapi import FastAPI
from typing import Optional

app=FastAPI()

product=[
    {'id':1,'types':"Pen","Price":100},
    {'id':2,'types':"Mobile","Price":25000},
    {'id':3,'types':"Laptop","Price":50000},
    {'id':4,'types':"Pen","Price":10},
    {'id':5,'types':"Mobile","Price":10000},
    {'id':6,'types':"Pen","Price":50}
]

@app.get('/product/')

def search(types:Optional[str]=None,price:Optional[int]=None):
    filter=product
    if types:#we use list comprehension that is p  for p in filter if this lne is list comprehension 
        filter =[p for p in filter if p['types'].lower() == types.lower()]#searching
    if price:
        filter =[p for p in filter if p['Price']<=price]#filtering
    return filter 


#optional with none
@app.get('/items/')

def name_get(name:Optional[str] = None):

    if name:
        return{
            "items_name":name
        }
    return{
        "Message":"Not passed Query Parameter"
    }

#localhost:8000/items

#localhost:8000/items/?name=shoes

#optional and Default value
@app.get('/product/')

def default(default_value :str = "all"):
    return{
        "Product":default_value
    }

#localhost:8000/product/?default_value=shoes



#localhost:8000/product

#Required Query parameter

@app.get('/required/')

def search_pass(cat:str):
    return{
        "items":cat
    }

#localhost:8000/required/?cat=laptop

#multiple parametrs

@app.get('/result/')

def search_passs(cat:str,price:int):
    return{
        "items":cat,
        "price":price
    }

#http://127.0.0.1:8000/result/?cat=laptop&price=1000


#Required + Optional
@app.get('/hello/')

def search_passes(cat:str,price:Optional[int]=None):
  if price:
      return{
          "Catagoery":cat,
          "price":price
      }
  return{
      "catagoery":cat,"price":"Price not mentioned"
  }

#http://127.0.0.1:8000/hello/?cat=laptop&price=1000

#http://127.0.0.1:8000/hello/?cat=laptop

#Convert to Lowercase

@app.get('/lower/')

def lower_case(lower_c:str):
    name=lower_c.lower()
    if name == "laptop":
        return {"item": "Laptop", "status": "Available"}
    elif name == "mobile":
        return {"item": "Mobile", "status": "Out of Stock"}
    else:
        return {"item": name, "status": "Not Found"}
    
#http://127.0.0.1:8000/lower/?lower_c=Laptop
#output
# {
#   "item": "Laptop",
#   "status": "Available"
# }
#http://127.0.0.1:8000/lower/?lower_c=LAPTOP
#output
# {
#   "item": "Laptop",
#   "status": "Available"
# }
#http://127.0.0.1:8000/lower/?lower_c=laptop
#output
# {
#   "item": "Laptop",
#   "status": "Available"
# }
#http://127.0.0.1:8000/lower/?lower_c=keyboard

items = {
    "laptop": {"item": "Laptop", "status": "Available"},
    "mobile": {"item": "Mobile", "status": "Out of Stock"},
    "tablet": {"item": "Tablet", "status": "Coming Soon"},
}

@app.get("/items/")
def get_items(name: str):
    # Convert input to lowercase
    item_name = name.lower()
    return items.get(item_name, {"item": name, "status": "Not Found"})

#sorting
@app.get("/sort/")
def sort_items(order: str = "asc"):
    items = [
        {"name": "Laptop", "price": 50000},
        {"name": "Phone", "price": 20000},
        {"name": "Tablet", "price": 30000},
    ]
    if order == "desc":
        items.sort(key=lambda x: x["price"], reverse=True)
    else:
        items.sort(key=lambda x: x["price"])
    return {"results": items}
#http://localhost:8000/sort/?order=desc
