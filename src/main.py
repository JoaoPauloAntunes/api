from typing import (
    List,
    Any
)

from fastapi import (
    Depends, 
    FastAPI, 
    HTTPException,
)
from fastapi import status
from fastapi import responses
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/")
def root():
    response = RedirectResponse("/docs")
    return response


@app.post("/users/", response_model=schemas.User)
def create_user(
    user: schemas.UserCreate, 
    db: Session = Depends(get_db)
):
    """
    Create a user.
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    """
    Read users.
    """
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(
    user_id: int, 
    db: Session = Depends(get_db)
):
    """
    Read a user.
    """
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(
    user_id: int, 
    user_in: schemas.UserUpdate,
    db: Session = Depends(get_db)
) -> Any:
    """
    Update a user.
    """
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return crud.update_user(db=db, db_user=db_user, user_in=user_in)


@app.delete("/users/{user_id}", response_model=schemas.User)
def remove_user(
    user_id: int, 
    db: Session = Depends(get_db)
) -> Any:
    """
    Remove a user.
    """
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return crud.remove_user(db=db, user_id=user_id)


@app.post("/users/{user_id}/requisitions/", response_model=schemas.Requisition)
def create_requisition_for_user(
    user_id: int, requisitions: schemas.RequisitionCreate, db: Session = Depends(get_db)
):
    """
    Create an requisition for a user.
    """
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return crud.create_user_requisition(db=db, requisitions=requisitions, user_id=user_id)


@app.get("/requisitions/", response_model=List[schemas.Requisition])
def read_requisitions(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    """
    Read requisitions.
    """
    requisitions = crud.get_requisitions(db=db, skip=skip, limit=limit)
    return requisitions


@app.get("/requisitions/{requisition_id}", response_model=schemas.Requisition)
def read_requisition(
    requisition_id: int, 
    db: Session = Depends(get_db)
) -> Any:
    """
    Read an requisition.
    """
    db_requisition = crud.get_requisition(db=db, requisition_id=requisition_id)
    if db_requisition is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Requisition not found")
    return db_requisition


@app.delete("/requisitions/{requisition_id}", response_model=schemas.Requisition)
def remove_requisition(
    requisition_id: int, 
    db: Session = Depends(get_db)
) -> Any:
    """
    Remove an requisition.
    """
    db_requisition = crud.get_requisition(db=db, requisition_id=requisition_id)
    if db_requisition is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Requisition not found")
    db_requisition = crud.remove_requisition(db=db, requisition_id=requisition_id)
    return db_requisition


@app.put("/requisitions/{requisition_id}", response_model=schemas.Requisition)
def update_requisition(
    requisition_id: int, 
    requisition_in: schemas.RequisitionUpdate,
    db: Session = Depends(get_db)
) -> Any:
    """
    Update an requisition.
    """
    db_requisition = crud.get_requisition(db=db, requisition_id=requisition_id)
    if db_requisition is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Requisition not found")
    return crud.update_requisition(db=db, db_requisition=db_requisition, requisition_in=requisition_in)