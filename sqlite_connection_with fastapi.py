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
#tables.py 
from sqlmodel import SQLModel,Field
from typing import Optional
from pydantic import EmailStr

class User(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    name:str
    phone:int
    email:EmailStr

class Createuser(SQLModel):
    name:str
    phone:int
    email:EmailStr
