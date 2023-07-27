import itertools
from fastapi import Form
from pydantic import BaseModel
from typing import List, Optional


id_counter = itertools.count(start=1)


class Todo(BaseModel):
    id: Optional[int]
    item: str

    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(id=next(id_counter), item=item)


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
