from typing import Annotated
from pydantic import Field, PositiveFloat

from models.db.BaseSchema import BaseSchema

class AthleteRequest(BaseSchema):
    name: Annotated[str, Field(description="Nome do atleta", example="Pedro Cunha", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="12345678901", max_length=11)]
    age: Annotated[int, Field(description="Idade do atleta", example=37, max_length=3)]
    weight: Annotated[PositiveFloat, Field(description="Peso do atleta", example=80.53, max_length=4, decimal_places=2)]
    height: Annotated[float, Field(description="Altura do atleta", example=1.80, max_length=3, decimal_places=2)]
    sex: Annotated[str, Field(description="Sexo do atleta", example="M", max_length=1)]
    training_center_id: int
    category_id: int