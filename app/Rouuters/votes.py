from fastapi import APIRouter, HTTPException
from .. import  database, models
from sqlalchemy.orm import Session
from fastapi import Body, Depends, status
from sqlalchemy import func


router = APIRouter(

    prefix='/gethotels',
    tags=['Get Hotels']
)


@router.get("/hotels/", status_code=status.HTTP_200_OK)
def get_hotels(db: Session = Depends(database.get_db)):
    hotels = db.query(models.Posts).all()
    result = []
    for hotel in hotels:
        h = {
            'id': hotel.id,
            'name': hotel.name,
            'location': hotel.location,
            'mobile_number': hotel.mobile_number,
            'hotel_pic': hotel.hotel_pic,
            'hotel_type': hotel.hotel_type,
            'created_at': hotel.created_at,
            'views':hotel.view_count,
            'google_maps_location':hotel.google_maps_location,
            'pictures': [],
            'packages': [],
            'features': []
        }
        pictures = db.query(models.HotelPictures).filter(models.HotelPictures.hotel_id == hotel.id).all()
        h['pictures'] = [{'id': picture.id, 
                          'picture': picture.picture,
                          'hotel_id': picture.hotel_id,
                           } for picture in pictures ]

        packages = db.query(models.Packages).filter(models.Packages.hotel_id == hotel.id).all()
        h['packages'] = []
        if packages:
            for package in packages:
                package_dict = {
                    'package_name': package.package_name, 
                    'charges_per_head_without_food': package.charges_per_head_without_food,
                    'charges_per_head_with_food': package.charges_per_head_with_food,
                    'food_served': package.food_served, 
                    'free_wifi': package.free_wifi, 
                    'stage_decoration': package.stage_decoration, 
                    'sound_system': package.sound_system, 
                    'ground_lighting': package.ground_lighting,
                    'bridal_room': package.bridal_room,
                    'free_parking': package.free_parking,
                    'chiller': package.chiller,
                    'heater': package.heater,
                    'package_picture': []
                }
                package_pictures = db.query(models.PackagePictures).filter(models.PackagePictures.package_id == package.id).all()
                package_dict['package_pictures'] = [{'id': picture.id, 
                                                     'picture': picture.picture, 
                                                     'package_id': picture.package_id
                                                    } for picture in package_pictures ]
                h['packages'].append(package_dict)

        features = db.query(models.HotelFeatures).filter(models.HotelFeatures.hotel_id == models.Posts.id).all()
        
        h['features'] = [ {'id': feature.id, 
                          'parking': feature.parking,
                          'child_playarea': feature.child_playarea,
                          'ground_lighting': feature.ground_lighting, 
                          'chiller': feature.chiller, 
                          'sound_system': feature.sound_system, 
                          'bridal_system': feature.bridal_system, 
                          'hotel_id': feature.hotel_id,
                           } for feature in features ]

        result.append(h)

    if not result:
        raise HTTPException(status_code=404, detail="No hotels found.")
    return result




@router.get("/hotels/search", status_code=status.HTTP_200_OK)
def get_hotels(location: str = None, db: Session = Depends(database.get_db)):
    hotels_query = db.query(models.Posts)
    if location:
        hotels_query = hotels_query.filter(func.lower(models.Posts.location).ilike(f'%{location.lower()}%')|func.lower(models.Posts.name).ilike(f'%{location.lower()}%'))
    hotels = hotels_query.all()
    result = []
    for hotel in hotels:
        h = {
            'id': hotel.id,
            'name': hotel.name,
            'location': hotel.location,
            'mobile_number': hotel.mobile_number,
            'hotel_pic': hotel.hotel_pic,
            'hotel_type': hotel.hotel_type,
            'created_at': hotel.created_at,
            'views':hotel.view_count,
            'pictures': [],
            'packages': [],
            'features': []
        }
        pictures = db.query(models.HotelPictures).filter(models.HotelPictures.hotel_id == hotel.id).all()
        h['pictures'] = [{'id': picture.id, 
                          'picture': picture.picture,
                          'hotel_id': picture.hotel_id,
                           } for picture in pictures ]

        packages = db.query(models.Packages).filter(models.Packages.hotel_id == hotel.id).all()
        h['packages'] = []
        if packages:
            for package in packages:
                package_dict = {
                    'package_name': package.package_name, 
                    'charges_per_head_without_food': package.charges_per_head_without_food,
                    'charges_per_head_with_food': package.charges_per_head_with_food,
                    'food_served': package.food_served, 
                    'free_wifi': package.free_wifi, 
                    'stage_decoration': package.stage_decoration, 
                    'sound_system': package.sound_system, 
                    'ground_lighting': package.ground_lighting,
                    'bridal_room': package.bridal_room,
                    'free_parking': package.free_parking,
                    'chiller': package.chiller,
                    'heater': package.heater,
                    'package_picture': []
                }
                package_pictures = db.query(models.PackagePictures).filter(models.PackagePictures.package_id == package.id).all()
                package_dict['package_pictures'] = [{'id': picture.id, 
                                                     'picture': picture.picture, 
                                                     'package_id': picture.package_id
                                                    } for picture in package_pictures ]
                h['packages'].append(package_dict)

        features = db.query(models.HotelFeatures).filter(models.HotelFeatures.hotel_id == hotel.id).all()
        
        h['features'] = [ {'id': feature.id, 
                          'parking': feature.parking,
                          'child_playarea': feature.child_playarea,
                          'ground_lighting': feature.ground_lighting, 
                          'chiller': feature.chiller, 
                          'sound_system': feature.sound_system, 
                          'bridal_system': feature.bridal_system, 
                          'hotel_id': feature.hotel_id,
                           } for feature in features ]

        result.append(h)

    if not result:
        raise HTTPException(status_code=404, detail="No hotels found.")
    return result


@router.post("/hotels/{hotel_id}/view-count/")
def increment_view_count(hotel_id: int,db: Session = Depends(database.get_db)):
    hotel = db.query(models.Posts).filter(models.Posts.id == hotel_id).first()
    if hotel:
        hotel.view_count += 1
        db.add(hotel)
        db.commit()
        return {"message": "View count incremented successfully"}
    else:
        raise HTTPException(status_code=404, detail="Hotel not found")




    