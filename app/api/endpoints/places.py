from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import place
from app.crud import crud_place 
from app.api import deps
from app.models.user import User

router = APIRouter()

@router.get("/places/",response_model=List[place.Place])
def read_place(db:Session = Depends(deps.get_db), skip: int = 0, limit: int = 10,current_user: User = Depends(deps.get_current_user),)->Any:
    return crud_place.get_places(db=db, skip=skip, limit=limit)

@router.post("/places/", response_model=place.Place)
def create_item(*,db: Session = Depends(deps.get_db),place_in: place.PlaceCreate,current_user: User = Depends(deps.get_current_user)) -> Any:
   place = crud_place.create_place(db=db,place=place_in)
   return place

@router.put("/places/{id}", response_model=place.Place)
def update_place(*,db: Session = Depends(deps.get_db),id: int,place_in: place.PlaceUpdate,current_user: User = Depends(deps.get_current_user),) -> Any:
  
   placeInDB = crud_place.get(db=db, place_id=id)
   if not placeInDB:
       raise HTTPException(status_code=404, detail="Place not found")
  
   place = crud_place.update_place(db=db,db_obj=placeInDB,obj_in=place_in)
   return place

@router.get("/places/{id}", response_model=place.Place)
def read_place(*,db: Session = Depends(deps.get_db),id: int,current_user: User = Depends(deps.get_current_user),) -> Any:
 
   place = crud_place.get(db=db, place_id=id)
   if not place:
       raise HTTPException(status_code=404, detail="Place not found")
   return place

@router.delete("/places/{id}", response_model=place.Place)
def delete_item(*,db: Session = Depends(deps.get_db),id: int,current_user: User = Depends(deps.get_current_user),) -> Any:
 
   place = crud_place.get(db=db, place_id=id)
   if not place:
       raise HTTPException(status_code=404, detail="Place not found")
 
   place = crud_place.delete_place(db=db,id=id)
   return place