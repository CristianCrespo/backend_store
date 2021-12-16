from typing import Optional
from pydantic import BaseModel, AnyHttpUrl

class PlaceBase(BaseModel):
    name: str
    price: Optional[int] = 0
    image: Optional[AnyHttpUrl]

class PlaceCreate(PlaceBase):
    pass

class PlaceUpdate(PlaceBase):
    pass

class PlaceInDBBase(PlaceBase):
    id: int

    class Config:
        orm_mode = True

class Place (PlaceInDBBase):
    pass

class PlaceInDB(PlaceInDBBase):
    pass