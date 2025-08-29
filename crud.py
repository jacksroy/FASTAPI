from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,EmailStr

app=FastAPI()

user_details={}
count_id=1

class User(BaseModel):
    name:str
    age:int
    price:float
    email:EmailStr#validate email

#pydantic model using post method
@app.post('/user/')
def user_data(data:User):
    global count_id
    user_details[count_id]=data
    
    response={
        "message":"user creared succesfully",
        "user_id":count_id,
        "user":user_details[count_id]
    }
    count_id +=1
    return response

#get method

@app.get("/getdata/")

def get_data():
    if not user_details:
        raise HTTPException(status_code=404,detail="User Not found")
    return user_details

#getting data using get

@app.get('/getdata/{user_id}')

def get_user(user_id:int):
    if user_id not in user_details:
        raise HTTPException(status_code=404,detail="User Not found")
    return user_details[user_id]

@app.put("/getdata/{user_id}")

def update_data(user_id:int,data:User):
    if user_id not in user_details:
        raise HTTPException(status_code=404,detail="User Not found")
    user_details[user_id] =data
    return{
        "messsage":"user updated",
        "user":data
    }
@app.delete("/getdata/{user_id}")

def delete_data(user_id:int):
    if user_id not in user_details:
        raise HTTPException(status_code=404,detail="User Not found")
    delete=user_details.pop(user_id)
    return{
        "message":"user deleted successfully",
        "deleted user":delete
    }
