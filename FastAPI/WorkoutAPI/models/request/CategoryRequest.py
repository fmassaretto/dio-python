from typing import Annotated
from pydantic import  UUID7, Field

from FastAPI.WorkoutAPI.models import BaseSchema

class CategoryRequest(BaseSchema):
    id: UUID7
    name: Annotated[str, Field(description="Categoria do atleta", examples="Iniciante", max_length=10)]