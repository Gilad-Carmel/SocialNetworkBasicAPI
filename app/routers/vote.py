from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.params import Body
from sqlalchemy.orm import Session
from .. import models, schemas
from configuration import utils
from ..database import engine, get_db

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote():
    return