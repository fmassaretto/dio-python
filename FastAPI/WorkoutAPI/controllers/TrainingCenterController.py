from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, status, HTTPException
from pydantic import UUID4
from sqlalchemy import select

from models.db.TrainingCenter import TrainingCenter
from models.response.TrainingCenterResponse import TrainingCenterResponse
from models.request.TrainingCenterRequest import TrainingCenterRequest
from models.contrib.dependencies import DatabaseDependency


router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TrainingCenterResponse)
async def create(db_session: DatabaseDependency, training_center_request: TrainingCenterRequest = Body(...)) -> TrainingCenterResponse:
    trainingCenter_response = TrainingCenterResponse(id=uuid4(), created_at=datetime.now(), **training_center_request.model_dump())
    trainingCenter_db_model = TrainingCenter(**trainingCenter_response.model_dump())

    db_session.add(trainingCenter_db_model)

    await db_session.commit()

    return trainingCenter_response

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[TrainingCenterResponse])
async def get_all(db_session: DatabaseDependency) -> list[TrainingCenterResponse]:
    trainingCenter_response: list[TrainingCenterResponse] = (await db_session.execute(select(TrainingCenter))).scalars().all()

    return trainingCenter_response

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=TrainingCenterResponse)
async def get_by_id(id: UUID4, db_session: DatabaseDependency) -> TrainingCenterResponse:
    trainingCenter_response: TrainingCenterResponse = (await db_session.execute(select(TrainingCenter).filter_by(id=id))).scalar()

    if not trainingCenter_response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= f"TrainingCenter not found, id = {id}")

    return trainingCenter_response