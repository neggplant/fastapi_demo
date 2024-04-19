from fastapi import APIRouter
from pydantic import BaseModel

base_router = APIRouter()


class Item(BaseModel):
    user_id: str | None = None
    data: dict | None = None


def temp():
    print()
    print()
    print()
    print()


@base_router.get("/base")
async def base():
    print(1)
    print(1)
    temp()
    print(1)
    print(1)
