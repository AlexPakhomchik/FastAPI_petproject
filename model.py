from fastapi.openapi.models import Schema
from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str

    class Config:
        Schema_extra = {'Example': {'id': 1, 'item': 'Example schema'}}
