


from pydantic import BaseModel

from typing import List

class HotelPicture(BaseModel):
    picture: str


class Create_post(BaseModel):
    name: str
    location: str
    mobile_number: str
    hotel_pic: str
    hotel_type: bool
    pictures: List[HotelPicture]


class CreateHotelFeatures(BaseModel):
    parking: bool = False
    child_playarea: bool = False
    ground_lighting: bool = False
    chiller: bool = False
    sound_system: bool = False
    bridal_system: bool = False

class CreatePackage(BaseModel):
    package_name: str
    charges_per_head_without_food: int
    charges_per_head_with_food: int
    food_served: str
    free_wifi: bool = False
    stage_decoration: bool = False
    sound_system: bool = False
    ground_lighting: bool = False
    bridal_room: bool = False
    free_parking: bool = False
    chiller: bool = False
    heater: bool = False
    hotel_id: int


class ReturnUser(BaseModel):
    id: int
    message: str = "OTP verified successfully"


class ReturnPost(BaseModel):
    id: int
    name: str
    location: str
    mobile_number: str
    hotel_pic: str
    hotel_type: bool
    created_at: str
    owner_id: int
    pictures: List[HotelPicture]


class CreateUser(BaseModel):
    otp:str
    phone_number:str     


class HotelFeatures(BaseModel):
    parking: bool = False
    child_playarea: bool = False
    ground_lighting: bool = False
    chiller: bool = False
    sound_system: bool = False
    bridal_system: bool = False

class HotelPictures(BaseModel):
    picture: str

class Packages(BaseModel):
    package_name: str
    charges_per_head_without_food: int
    charges_per_head_with_food: int
    food_served: str
    free_wifi: bool = False
    stage_decoration: bool = False
    sound_system: bool = False
    ground_lighting: bool = False
    bridal_room: bool = False
    free_parking: bool = False
    chiller: bool = False
    heater: bool = False
    hotel_id: int

class GetHotelDetails(BaseModel):
    id: int
    name: str
    location: str
    mobile_number: str
    hotel_pic: str
    hotel_type: bool
    created_at: str
    owner_id: int
   