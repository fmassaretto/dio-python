from typing import Annotated, Optional
from pydantic import Field, PositiveFloat

from models.request.CategoryRequest import CategoryRequest
from models.request.TrainingCenterRequest import TrainingCenterNameRequest
from models.db.BaseSchema import BaseSchema

class AthleteRequest(BaseSchema):
    name: Annotated[str, Field(description="Nome do atleta", example="Pedro Cunha", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="12345678901", max_length=11)]
    age: Annotated[int, Field(description="Idade do atleta", example=37)]
    weight: Annotated[PositiveFloat, Field(description="Peso do atleta", example=80.53)]
    height: Annotated[float, Field(description="Altura do atleta", example=1.80)]
    sex: Annotated[str, Field(description="Sexo do atleta", example="M", max_length=1)]
    category: Annotated[CategoryRequest, Field(description='Athlete category')]
    training_center: Annotated[TrainingCenterNameRequest, Field(description='Athlete\'s training center')]

class AthleteUpdateRequest(BaseSchema):
    name: Annotated[Optional[str], Field(None, description="Nome do atleta", example="Pedro Cunha", max_length=50)]
    age: Annotated[Optional[int], Field(None, description="Idade do atleta", example=37)]
