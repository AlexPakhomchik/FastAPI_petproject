from pydantic import BaseModel
from typing import List


class Todo(BaseModel):
    id: int
    item: str

    class Config:
        json_schema_extra = {
            'Example': {
                'id': 1,
                'item': 'Example schema'
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {'Example': {'item': 'example'}}


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {"example": {"todos":
            [
                {
                    "item": "Example schema 1!"
                },
                {
                    "item": "Example schema 2!"
                }
            ]
        }
        }
