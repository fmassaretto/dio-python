from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, status, HTTPException
from pydantic import UUID4
from sqlalchemy import select

from models.db.Category import Category
from models.response.CategoryResponse import CategoryResponse
from models.request.CategoryRequest import CategoryRequest
from models.contrib.dependencies import DatabaseDependency


router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CategoryResponse)
async def create(db_session: DatabaseDependency, category_request: CategoryRequest = Body(...)) -> CategoryResponse:
    category_response = CategoryResponse(id=uuid4(), created_at=datetime.now(), **category_request.model_dump())
    category_db_model = Category(**category_response.model_dump())

    db_session.add(category_db_model)

    await db_session.commit()

    return category_response

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[CategoryResponse])
async def get_all(db_session: DatabaseDependency) -> list[CategoryResponse]:
    categories_response: list[CategoryResponse] = (await db_session.execute(select(Category))).scalars().all()

    return categories_response

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=CategoryResponse)
async def get_by_id(id: UUID4, db_session: DatabaseDependency) -> CategoryResponse:
    category_response: CategoryResponse = (await db_session.execute(select(Category).filter_by(id=id))).scalar()

    if not category_response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= f"Category not found, id = {id}")

    return category_response
