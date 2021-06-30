from typing import Dict, Union, Any
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from .models import user_models, requisition_models 
from .schemas import user_schemas, requisition_schemas

def get_user(
    db: Session, 
    user_id: int
):
    return db.query(user_models.User).filter(user_models.User.id == user_id).first()
    

def remove_user(
    db: Session, 
    user_id: int
):
    db_user = db.query(user_models.User).get(user_id)
    db.delete(db_user)
    db.commit()
    return db_user


def update_user(
    db: Session, 
    db_user: user_models.User, 
    user_in = Union[user_schemas.UserUpdate, Dict[str, Any]]
):
    user_data = jsonable_encoder(db_user)
    print({"user_data": user_data})

    if isinstance(user_in, dict):
        update_data = user_in
    else:
        update_data = user_in.dict(exclude_unset = True)
    print({"update_data": update_data})
    
    if update_data.get("password", None):
        fake_hashed_password = update_data["password"] + "notreallyhashed"
        del update_data["password"]
        update_data["hashed_password"] = fake_hashed_password

    print({"update_data": update_data})
    
    for field in user_data:
        field_value = update_data.get(field, None)
        if field_value is not None:
            setattr(db_user, field, field_value)

    user_data = jsonable_encoder(db_user)
    print({"user_data": user_data})

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_email(
    db: Session, 
    email: str
):
    return db.query(user_models.User).filter(user_models.User.email == email).first()


def get_users(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
):
    return db.query(user_models.User).offset(skip).limit(limit).all()


def create_user(
    db: Session, 
    user: user_schemas.UserCreate
):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = user_models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_requisition(
    db: Session,
    reqn: int
):
    return db.query(requisition_models.Requisition).filter(requisition_models.Requisition.reqn == reqn).first()
    

def remove_requisition(
    db: Session, 
    reqn: int
):
    db_requisition = db.query(requisition_models.Requisition).get(reqn)
    db.delete(db_requisition)
    db.commit()
    return db_requisition


def update_requisition(
    db: Session, 
    db_requisition: requisition_models.Requisition, 
    requisition_in = Union[requisition_schemas.RequisitionUpdate, Dict[str, Any]]
):
    requisition_data = jsonable_encoder(db_requisition)
    print({"requisition_data": requisition_data})

    if isinstance(requisition_in, dict):
        update_data = requisition_in
    else:
        update_data = requisition_in.dict(exclude_unset = True)
    print({"update_data": update_data})
    
    for field in requisition_data:
        field_value = update_data.get(field, None)
        if field_value is not None:
            setattr(db_requisition, field, field_value)

    requisition_data = jsonable_encoder(db_requisition)
    print({"requisition_data": requisition_data})

    db.add(db_requisition)
    db.commit()
    db.refresh(db_requisition)

    return db_requisition


def get_requisitions(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
):
    return db.query(requisition_models.Requisition).offset(skip).limit(limit).all()


def create_user_requisition(
    db: Session, 
    requisition: requisition_schemas.RequisitionCreate, 
    user_id: int
):
    db_requisition = requisition_models.Requisition(**requisition.dict(), owner_id=user_id)
    db.add(db_requisition)
    db.commit()
    db.refresh(db_requisition)
    return db_requisition
