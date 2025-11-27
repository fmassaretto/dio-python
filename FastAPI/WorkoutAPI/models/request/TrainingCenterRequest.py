from typing import Annotated
from pydantic import Field

from models.db.BaseSchema import BaseSchema

class TrainingCenterRequest(BaseSchema):
    name: Annotated[str, Field(description="Nome do centro de treinamento", example="SESI", max_length=20)]
    address: Annotated[str, Field(description="Endereço do centro de treinamento", example="Rua 15 de maio, 123 / Cidade - Estado", max_length=60)]
    owner: Annotated[str, Field(description="Proprietario do centro de treinamento", example="Mario Silva", max_length=30)]