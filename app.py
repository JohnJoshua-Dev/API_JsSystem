import uvicorn
from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

# Data Base
DATABASE_URL="mysql+pymysql://joshuadev:JsDevelopment@localhost/testAPI"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


# Models
class Cliente(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email =Column(String, unique=True, index=True)

# Esquemas para Validacao
class ClienteCreate(BaseModel):
    name:str
    email:str

class ClienteResponse(ClienteCreate):
    id:int
    name:str
    email:str

    class config:
        from_attributes=True


# Main Aplicacao

app = FastAPI()

Base.metadata.create_all(bind=engine)
    # dependencias para obtercessao.
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

# endpoints
@app.get("/")
def read_root():
    return {"Hello": "API Working"}

if __name__ == "__main__":
  
    uvicorn.run(app, port=8000)
  