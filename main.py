from fastapi import FastAPI

app=FastAPI()

@app.get('/greet')

def first():
    return{
        'message':" Welcome to FastAPI for First Time"
    }