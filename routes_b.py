from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from database import get_session

router = APIRouter(prefix="/resursi_b", tags=["Resurs B"])