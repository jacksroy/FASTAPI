from fastapi import FastAPI

app=FastAPI()

@app.get('/greet{name}')

def first(name:str):
    return{
        'message':f"{name} Welcome to FastAPI for First Time"
    }
