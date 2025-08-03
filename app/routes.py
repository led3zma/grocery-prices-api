from typing import Annotated
from app.database import SessionDep
from app.models import Category, CategoryBase
import app.crud as crud

from fastapi import APIRouter, Body, Path

router = APIRouter()

# Category Router

category_router = APIRouter(prefix='/categories', tags=['category'])


@category_router.get('/')
async def read_categories(session: SessionDep) -> list[Category]:
    return crud.read_categories(session)


@category_router.get('/{category_id}')
async def read_category(category_id: Annotated[int, Path(gt=0)], session: SessionDep) -> Category:
    return crud.read_category(category_id, session)


@category_router.post('/')
async def create_category(category: Annotated[CategoryBase, Body()], session: SessionDep) -> Category:
    return crud.create_category(category, session)


@category_router.patch('/{category_id}')
async def update_category(category_id: Annotated[int, Path(gt=0)], category: Annotated[CategoryBase, Body()], session: SessionDep) -> Category:
    return crud.update_category(category_id, category, session)


@category_router.delete('/{category_id}')
async def delete_category(category_id: Annotated[int, Path(gt=0)], session: SessionDep) -> dict:
    if not crud.delete_category(category_id, session):
        return {'result': 'False'}
    return {'result': 'ok'}

router.include_router(category_router)
