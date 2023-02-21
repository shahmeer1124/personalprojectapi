from .database import Base
from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, LargeBinary, String, ForeignKey
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship



class HotelPictures(Base):
    __tablename__ = 'hotel_pictures'
    id = Column(Integer, primary_key=True, nullable=False)
    picture = Column(String, nullable=False)
    hotel_id = Column(Integer, ForeignKey(
    'posts.id', ondelete='CASCADE'), nullable=False)

class Posts(Base):
        __tablename__ = 'posts'
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String, nullable=False)
        location = Column(String, nullable=False)
        mobile_number = Column(String, nullable=False)
        view_count = Column(Integer, default=0)
        google_maps_location = Column(String)
        hotel_pic = Column(String, nullable=False)
        hotel_type = Column(Boolean, default=False, nullable=False)
        created_at = Column(TIMESTAMP(timezone=True),
                            nullable=False, server_default=func.now())
        owner_id = Column(Integer, ForeignKey(
            'users.id', ondelete='CASCADE'), nullable=False, unique=True)
        user = relationship("User")
        pictures = relationship(
            "HotelPictures", cascade="all, delete, delete-orphan")

class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True, nullable=False)
        phone_number = Column(String, nullable=False, unique=True)
        created_at = Column(TIMESTAMP(timezone=True),
                            nullable=False, server_default=func.now())

class HotelFeatures(Base):
        __tablename__ = 'hotel_features'
        id = Column(Integer, primary_key=True, nullable=False)
        parking = Column(Boolean, default=False, nullable=False)
        child_playarea = Column(Boolean, default=False, nullable=False)
        ground_lighting = Column(Boolean, default=False, nullable=False)
        chiller = Column(Boolean, default=False, nullable=False)
        sound_system = Column(Boolean, default=False, nullable=False)
        bridal_system = Column(Boolean, default=False, nullable=False)
        hotel_id = Column(Integer, ForeignKey(
            'posts.id', ondelete='CASCADE'), nullable=False)

class Packages(Base):
        __tablename__ = 'packages'
        id = Column(Integer, primary_key=True, nullable=False)
        package_name = Column(String, nullable=False)
        charges_per_head_without_food = Column(String, nullable=False)
        charges_per_head_with_food = Column(String, nullable=False)
        food_served = Column(String, nullable=False)
        free_wifi = Column(Boolean, default=False, nullable=False)
        stage_decoration = Column(Boolean, default=False, nullable=False)
        sound_system = Column(Boolean, default=False, nullable=False)
        ground_lighting = Column(Boolean, default=False, nullable=False)
        bridal_room = Column(Boolean, default=False, nullable=False)
        free_parking = Column(Boolean, default=False, nullable=False)
        chiller = Column(Boolean, default=False, nullable=False)
        heater = Column(Boolean, default=False, nullable=False)
        hotel_id = Column(Integer, ForeignKey(
            'posts.id', ondelete='CASCADE'), nullable=False)


class PackagePictures(Base):
    __tablename__ = 'package_pictures'
    id = Column(Integer, primary_key=True, nullable=False)
    picture = Column(String, nullable=False)
    package_id = Column(Integer, ForeignKey('packages.id', ondelete='CASCADE'), nullable=False)
    package = relationship("Packages")