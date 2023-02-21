from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import setting

"postgresql://username:password@host:port/database"

# Connection with the database using sql alchemy
connection_string = f"postgresql://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}"
engine = create_engine(connection_string)
Session_Local = sessionmaker(autocommit=False,autoflush=False, bind=engine)

# This session is used to add delete update record inside the database
# session = Session()


# creating the session which is used to create a record delete record update record
def get_db():
    db = Session_Local()
    try:
        yield db
    finally:
        db.close()



# This base is used to create the tables and define the columns inside the databse
Base=declarative_base()


