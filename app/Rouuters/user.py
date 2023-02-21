from fastapi import Body, Depends,status,HTTPException,APIRouter

from .. import schema
from .. import models
from sqlalchemy.orm import Session
import requests
from ..database import get_db

router=APIRouter(
    prefix='/users',
    tags=['Users']
)





@router.post("/")
def send_otp(phone_number: str):
    # Send OTP to user's phone number using Sinch API
    response = send_sms(phone_number)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to send OTP")
    return {"message": "OTP sent successfully"}

def send_sms(phone_number):
    url = "https://verification.api.sinch.com/verification/v1/verifications"
    applicationKey = "fac9bfae-8cd8-4af2-985d-a43284ea06aa"
    applicationSecret = "/DP4OmrTBUSaoqdHLVum4w=="
    headers = {"Content-Type": "application/json"}
    payload = {
    "identity": {
        "type": "number",
        "endpoint": phone_number
    },
    "method": "sms"
}
    response = requests.post(url, json=payload, headers=headers, auth=(applicationKey, applicationSecret))
    
    return response




#path operation to verify otp
@router.post("/verify",response_model=schema.ReturnUser,status_code=status.HTTP_201_CREATED)
def verify_otp(user:schema.CreateUser,otp: str, phone_number: str,db: Session = Depends(get_db)):
    # Verify OTP using Sinch API
    response = verify_sinch_otp(user.otp, user.phone_number)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to verify OTP")
    # Retrieve user data from response
    user_data = response.json()
    # Create a new user in the database
    new_user = models.User(**user_data)
    db.add(new_user)
    db.commit()
    return {"message": "OTP verified successfully"}
    

def verify_sinch_otp(otp, phone_number):
    applicationKey = "fac9bfae-8cd8-4af2-985d-a43284ea06aa"
    applicationSecret = "/DP4OmrTBUSaoqdHLVum4w=="
    url = "https://verification.api.sinch.com/verification/v1/verifications/number/" + phone_number
    payload = {
    "method": "sms",
    "sms": {
        "code": otp
    }
}
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, json=payload, headers=headers, auth=(applicationKey, applicationSecret))
    return response


















