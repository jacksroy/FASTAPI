#pip install python-multipart

from fastapi import FastAPI,Depends,HTTPException,Form,File,UploadFile
from sqlmodel import SQLModel,create_engine,Session,select
from typing import Annotated
from pydantic import EmailStr
from contextlib import asynccontextmanager
from tables import User,Createuser
import os,shutil

DATABASE_URL="sqlite:///./user.db"

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

Uploads_dirs="uploads"
os.makedirs(Uploads_dirs,exist_ok=True)

@app.post("/creteausers")

def userdata(
    session:SessionDep,
    name:str=Form(...),
    phone:int=Form(...),
    email:EmailStr=Form(),
    file:UploadFile=File(...)):

    user_data={"name":name,"phone":phone,"email":email}
    validate_data=Createuser.model_validate(user_data)
    file_path=os.path.join(Uploads_dirs,file.filename)
    with open(file_path,"wb") as f:
        shutil.copyfileobj(file.file ,f)

    user=User(**validate_data.model_dump(),file_path=f"{Uploads_dirs}/{file.filename}")

    session.add(user)
    session.commit()
    session.refresh(user)
    return user 

#tables.py

from sqlmodel import SQLModel,Field
from typing import Optional
from pydantic import EmailStr

class User(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    name:str
    phone:int
    email:EmailStr
    file_path:str

class Createuser(SQLModel):
    name:str
    phone:int
    email:EmailStr

