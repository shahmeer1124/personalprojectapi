
from fastapi import Body, Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine


from .database import get_db
from .Rouuters import post,user,votes



# creation of tables using Base this line will create all the tables that are mentioned inside models
models.Base.metadata.create_all(bind=engine)






app=FastAPI()
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(post.router)
# app.include_router(auth.router)
app.include_router(votes.router)



    





    
        













