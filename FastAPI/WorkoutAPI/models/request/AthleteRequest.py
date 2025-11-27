from typing import Annotated
from pydantic import UUID7, Field, PositiveFloat

from FastAPI.WorkoutAPI.models import BaseSchema

class AthleteRequest(BaseSchema):
    id: UUID7
    name: Annotated[str, Field(description="Nome do atleta", examples="Pedro Cunha", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", examples="12345678901", max_length=11)]
    age: Annotated[int, Field(description="Idade do atleta", examples=37, max_length=3)]
    weight: Annotated[PositiveFloat, Field(description="Peso do atleta", examples=80.53, max_length=4, decimal_places=2)]
    height: Annotated[float, Field(description="Altura do atleta", examples=1.80, max_length=3, decimal_places=2)]
    sex: Annotated[str, Field(description="Sexo do atleta", examples="M", max_length=1)]
    training_center_id: int
    category_id: int