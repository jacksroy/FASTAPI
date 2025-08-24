from fastapi import FastAPI


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

 
