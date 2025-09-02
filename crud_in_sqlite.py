from fastapi import FastAPI,Depends,HTTPException
from sqlmodel import SQLModel,create_engine,Session,select
from typing import Annotated
from contextlib import asynccontextmanager
from tables import User,Createuser

DATABASE_URL="sqlite:///./users.db"

engine=create_engine(DATABASE_URL,echo=True,connect_args={"check_same_thread":False})

@asynccontextmanager

async def lifespan(app:FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app=FastAPI(lifespan=lifespan)

def get_session():
    with Session(engine) as session:
        yield session
SessionDep =Annotated[Session,Depends(get_session)]

@app.post('/userdata')

def crete_user(user:Createuser,session:SessionDep):
    new_user=User.model_validate(user)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@app.get('/getuser',response_model=list[User])

def get_data( session:SessionDep):
    users=session.exec(select(User)).all()
    if not users:
        raise HTTPException(status_code=404,detail="User not found")
    return users 

@app.get('/getusers/{user_id}',response_model=User)

def get_single( user_id:int,session:SessionDep):
    user=session.get(User,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return user 

@app.put('/getusers/{user_id}',response_model=User)

def update_user( user_id:int,update:Createuser,session:SessionDep):
    user=session.get(User,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    user.name=update.name
    user.phone=update.phone
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.delete('/getusers/{user_id}')

def get_single( user_id:int,session:SessionDep):
    user=session.get(User,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    session.delete(user)
    session.commit()
    return{
        "message":"user deleted"
    }


