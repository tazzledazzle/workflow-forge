# pylint: disable=missing-function-docstring,missing-module-docstring,missing-class-docstring

from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str
