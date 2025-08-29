from fastapi import FastAPI,Body
from pydantic import BaseModel,Field
from typing import Optional,List

app=FastAPI()

# count=1
# user_details={}

class order(BaseModel):
    name:str
    price:float
    phone:int
    age:int=18
class product(BaseModel):
    order_id:int
    product_name:List[order]
    customer_name:str


# @app.post('/crete')

# def post_data(user:product):
#     global count
#     user_details[count]=user
#     count +=1
#     return user

# @app.get('/')

# def get_data():
#     return user_details

@app.post("/user/")
def create_user(user: dict = Body(...)):
    return {"message": "User created successfully", "user": user}

@app.post("/create")

def enter_data(pro:product):
    return{
        "message":"user created Succesfully",
        "user":pro
    }
#   for list
# #{
#   "order_id": 101,
#   "product_name": [
#     {
#       "name": "shoes",
#       "price": 199.0,
#       "phone": 9894575800,
#       "age": 18
#     },  {
#       "name": "mic",
#       "price": 20009.0,
#       "phone": 9894575800
#     }
#   ],
#   "customer_name": "jacks"
# }

#feild validation

class feild(BaseModel):
    name:int=Field(...,gt=0)
    phone:str=Field(...,min_length=6)
    age:Optional[int]=Field(18,ge=18,lt=100)

@app.post('/')

def feild_data(data:feild):
    return{
        "message":"successfully created",
        "Data":data
    }

class alis(BaseModel):
    full_name: str = Field(..., alias="fullName")
    age: int

@app.post("/create-user/")
def user_cre(user: alis):
    return user
