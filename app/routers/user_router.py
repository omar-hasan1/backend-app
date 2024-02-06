from fastapi import APIRouter, status
from app.models.user_model import User

router = APIRouter()

@router.post("/create_user", status_code=status.HTTP_200_OK)
async def create_user(user: User):
    # User creation logic goes here
    return {"message": "User is created"}
