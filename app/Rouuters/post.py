from typing import Optional,List
from fastapi import Body, Depends, FastAPI, Response,status,HTTPException,APIRouter
from sqlalchemy import null,func
from .. import schema
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .. import models
from ..database import Session_Local, engine
from sqlalchemy.orm import Session
from ..database import get_db
from . import oath2
from sqlalchemy.orm import joinedload
import json

router=APIRouter(
    prefix='/posts',
    tags=['Posts']
)
# creation of tables using Base this line will create all the tables that are mentioned inside models
models.Base.metadata.create_all(bind=engine)
# This is the path operation for creating the entry of a hotel  
@router.post('/')
def createpost(id: str, post: schema.Create_post, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    hotel_pictures = [models.HotelPictures(picture= picture.picture) for picture in post.pictures]
    newpost = models.Posts(
        name=post.name,
        location=post.location,
        mobile_number=post.mobile_number,
        hotel_pic=post.hotel_pic,
        hotel_type=post.hotel_type,
        owner_id=user.id,
        pictures=hotel_pictures
    )
    db.add(newpost)
    db.commit()
    db.refresh(newpost)
    return newpost.id
# The next path operation is going to add the hotel features 
@router.post('/{hotel_id}/features')
def create_hotel_features(hotel_id: int, features: schema.CreateHotelFeatures, db: Session = Depends(get_db)):
    hotel = db.query(models.Posts).filter(models.Posts.id == hotel_id).first()
    if not hotel:
        raise HTTPException(status_code=400, detail="Hotel not found") 
    new_features = models.HotelFeatures(
        parking=features.parking,
        child_playarea=features.child_playarea,
        ground_lighting=features.ground_lighting,
        chiller=features.chiller,
        sound_system=features.sound_system,
        bridal_system=features.bridal_system,
        hotel_id=hotel_id
    )
    db.add(new_features)
    db.commit()
    db.refresh(new_features)
    return {"id": new_features.id}
# path operation for creating the packages for the hotel
@router.post("/{hotel_id}/packages")
def create_package(hotel_id: int, package: schema.CreatePackage, db: Session = Depends(get_db)):
    hotel = db.query(models.Posts).filter(models.Posts.id == hotel_id).first()
    if not hotel:
        raise HTTPException(status_code=400, detail="Hotel not found")

    new_package = models.Packages(
        package_name=package.package_name,
        charges_per_head_without_food=package.charges_per_head_without_food,
        charges_per_head_with_food=package.charges_per_head_with_food,
        food_served=package.food_served,
        free_wifi=package.free_wifi,
        stage_decoration=package.stage_decoration,
        sound_system=package.sound_system,
        ground_lighting=package.ground_lighting,
        bridal_room=package.bridal_room,
        free_parking=package.free_parking,
        chiller=package.chiller,
        heater=package.heater,
        hotel_id=hotel_id
    )
    db.add(new_package)
    db.commit()
    db.refresh(new_package)
    return {"id": new_package.id}