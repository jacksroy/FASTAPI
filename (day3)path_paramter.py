from fastapi import FastAPI,HTTPException

app=FastAPI()

@app.get('/restaurant/{name}')

def first(name:str):
    restaurant=name.lower()


    if restaurant== "pizzahut":
        return{"restaurant": "PizzaHut",
               "status": "open",
               "menu":["Pizza", "Pasta", "Garlic Bread"]
}
    
    elif restaurant=="dominos" :
        return{
             "restaurant": "Dominos",
             "status": "closed",
            "menu": ["Veg Pizza", "Cheese Burst", "Brownie"]

        }
    else:
        return{
            "restaurant":name,
            "status":"unknown"
        }
    

user={
    1:{"name":"hello",
       "orders":{
           101:{
               "name":"laptop","amount":3700000
           },
           102:{
               "name":"jug","amount":908,
           }
       }
       
       },
    2:{"name":"welcome",
       "orders":{
           201:{
               "name":"mouse","amount":250,

           },
           202:{
               "name":"keyboard","amount":500
           }
       }
       }
}

@app.get("/users/{user_id}/order/{order_id}")
def get_data(user_id: int, order_id: int):
    if user_id not in user:
        raise HTTPException(status_code=404, detail="User not found")
    if order_id not in user[user_id]["orders"]:
        raise HTTPException(status_code=404, detail="Order not found")
    return user[user_id]["orders"][order_id]

 
@app.get("/user/{user_name}")

def get_data(user_name:str):
    
        user = user_name.lower()

        if user == "hello":
             return{
                  "name":"hello"
             }
        elif user == "guru":
             return{
                  "name":"guru"
             }
        else:
             return{
                  "name":"not found"
             }
        
@app.get('/id/{id}/id_name/{id_no}')

def get_id(id :int,id_name:str):
     return{
          "id":id,
          "id_name":id_name
     }

    
