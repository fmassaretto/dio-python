from datetime import datetime
from typing import Annotated

from pydantic import UUID4, Field


class BaseResponse():
    id: Annotated[UUID4, Field(description="ID")]
    created_at: Annotated[datetime, Field(description="Created at")]