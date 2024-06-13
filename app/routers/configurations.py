from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/configurations",
    tags=["configurations"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Configuration)
def create_configuration(config: schemas.ConfigurationCreate, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code=config.country_code)
    if db_config:
        raise HTTPException(status_code=400, detail="Configuration already exists")
    return crud.create_configuration(db=db, config=config)

@router.get("/{country_code}", response_model=schemas.Configuration)
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code=country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config

@router.post("/{country_code}", response_model=schemas.Configuration)
def update_configuration(country_code: str, config: schemas.ConfigurationUpdate, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code=country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return crud.update_configuration(db=db, country_code=country_code, config=config)

@router.delete("/{country_code}", response_model=schemas.Configuration)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code=country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return crud.delete_configuration(db=db, country_code=country_code)
