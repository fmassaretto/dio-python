from fastapi import APIRouter, Body, status

from models.response.AthleteResponse import AthleteResponse
from models.request.AthleteRequest import AthleteRequest
from models.contrib.dependencies import DatabaseDependency


router = APIRouter()

@router.post(path="/", status_code=status.HTTP_201_CREATED, response_model=AthleteResponse)
async def post(db_session: DatabaseDependency, athlete_request: AthleteRequest = Body(...)):
    ...
