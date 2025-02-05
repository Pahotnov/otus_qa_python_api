from typing import List, Dict
from pydantic import BaseModel


class DogApiResponseModel(BaseModel):
    message: str
    status: str


class DogApiListResponseModel(BaseModel):
    message: List | Dict
    status: str
