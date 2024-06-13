from pydantic import BaseModel
from typing import Dict, Any

class ConfigurationCreate(BaseModel):
    country_code: str
    configuration: Dict[str, Any]

class ConfigurationUpdate(BaseModel):
    configuration: Dict[str, Any]

class Configuration(BaseModel):
    id: int
    country_code: str
    configuration: Dict[str, Any]

    class Config:
        orm_mode = True
