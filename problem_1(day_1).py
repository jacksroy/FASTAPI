from fastapi import FastAPI


app=FastAPI()

@app.get('/restaurant/{name}')

def first(name:str):
    restaurant=name.lower()


    if restaurant== "pizzahut":
        return{"restaurant": "PizzaHut",
               "status": "open"
}
    
    elif restaurant=="dominos" :
        return{
             "restaurant": "Dominos",
             "status": "closed"

        }
    else:
        return{
            "restaurant":name,
            "status":"unknown"
        }

 
