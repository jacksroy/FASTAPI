from fastapi import FastAPI

app=FastAPI()

@app.get('/greet{name}')

def first(name:str):
    return{
        'message':f"{name} Welcome to FastAPI for First Time"
    }

@app.get('/square/{num}')

def sum(num:int):
    return{
        "result":f"{num * num} Area of Square"
    }
