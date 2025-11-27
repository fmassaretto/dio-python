from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select

from models.db.TrainingCenter import TrainingCenter
from models.db.Category import Category
from models.response.CategoryResponse import CategoryResponse
from models.db.Athlete import Athlete
from models.response.AthleteResponse import AthleteResponse
from models.request.AthleteRequest import AthleteRequest, AthleteUpdateRequest
from models.contrib.dependencies import DatabaseDependency


router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AthleteResponse)
async def create(db_session: DatabaseDependency, athlete_request: AthleteRequest = Body(...)) -> AthleteResponse:
    category_name = athlete_request.category.name
    training_center_name = athlete_request.training_center.name

    category_response = (await db_session.execute(select(Category).filter_by(name=category_name))).scalar()

    if not category_response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= f"Category not found, id = {id}")
    
    training_center_response = (await db_session.execute(
        select(TrainingCenter).filter_by(name=training_center_name))
    ).scalars().first()
    
    if not training_center_response:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=f'The training center {training_center_response} was not found.'
        )
    
    try:
        athlete_response = AthleteResponse(id=uuid4(), created_at=datetime.now(), **athlete_request.model_dump())
        athlete_db_model = Athlete(**athlete_response.model_dump(exclude={'category', 'training_center'}))

        athlete_db_model.category_id = category_response.pk_id
        athlete_db_model.training_center_id = training_center_response.pk_id


        db_session.add(athlete_db_model)

        await db_session.commit()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail='Failed to save to db'
        )

    return athlete_response

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[AthleteResponse])
async def get_all(db_session: DatabaseDependency) -> list[AthleteResponse]:
    athletes_response: list[AthleteResponse] = (await db_session.execute(select(Athlete))).scalars().all()

    return [AthleteResponse.model_validate(athletes) for athletes in athletes_response]

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=AthleteResponse)
async def get_by_id(id: UUID4, db_session: DatabaseDependency) -> AthleteResponse:
    athlete_response: AthleteResponse = (await db_session.execute(select(Athlete).filter_by(id=id))).scalar()

    if not athlete_response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= f"Athlete not found, id = {id}")

    return athlete_response

@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=AthleteResponse)
async def update_by_id(id: UUID4, db_session: DatabaseDependency, athlete_update_request: AthleteUpdateRequest = Body(...)) -> AthleteResponse:
    athlete_response: AthleteResponse = (await db_session.execute(select(Athlete).filter_by(id=id))).scalar()

    if not athlete_response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= f"Athlete not found, id = {id}")
    
    athlete_update = athlete_update_request.model_dump(exclude_unset=True)

    for key, value in athlete_update.items():
        setattr(athlete_response, key, value)

    await db_session.commit()
    await db_session.refresh(athlete_response)

    return athlete_response

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_by_id(id: UUID4, db_session: DatabaseDependency) -> None:
    athlete_response: AthleteResponse = (await db_session.execute(select(Athlete).filter_by(id=id))).scalar()

    if not athlete_response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= f"Athlete not found, id = {id}")

    await db_session.delete(athlete_response)
    await db_session.commit()
