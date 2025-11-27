from typing import Annotated
from pydantic import UUID7, Field

from FastAPI.WorkoutAPI.models import BaseSchema

class TrainingCenterRequest(BaseSchema):
    id: UUID7
    name: Annotated[str, Field(description="Nome do centro de treinamento", examples="SESI", max_length=20)]
    address: Annotated[str, Field(description="Endereço do centro de treinamento", examples="SESI", max_length=60)]
    owner: Annotated[str, Field(description="Proprietario do centro de treinamento", examples="Mario Silva", max_length=30)]