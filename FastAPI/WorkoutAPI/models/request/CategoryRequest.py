from typing import Annotated
from pydantic import Field

from models.db.BaseSchema import BaseSchema

class CategoryRequest(BaseSchema):
    name: Annotated[str, Field(description="Categoria do atleta", example="Iniciante", max_length=10)]