from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items")
def read_items(db: Session = Depends(get_db)):
    return crud.get_items(db)

@app.post("/items")
def create_item(name: str, db: Session = Depends(get_db)):
    return crud.create_item(db, name)
