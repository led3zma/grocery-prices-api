from typing import Annotated
from app.database import SessionDep
from app.models import Category, CategoryBase, CategoryUpdate, Store, StoreBase, StoreUpdate
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


@category_router.put('/{category_id}')
async def update_category(category_id: Annotated[int, Path(gt=0)], category: Annotated[CategoryUpdate, Body()], session: SessionDep) -> Category:
    return crud.update_category(category_id, category, session)


@category_router.delete('/{category_id}')
async def delete_category(category_id: Annotated[int, Path(gt=0)], session: SessionDep) -> dict:
    if not crud.delete_category(category_id, session):
        return {'result': 'False'}
    return {'result': 'ok'}

# Store Router

store_router = APIRouter(prefix='/stores', tags=['store'])


@store_router.get('/')
async def read_stores(session: SessionDep) -> list[Store]:
    return crud.read_stores(session)


@store_router.get('/{store_id}')
async def read_store(store_id: Annotated[int, Path(gt=0)], session: SessionDep) -> Store:
    return crud.read_store(store_id, session)


@store_router.post('/')
async def create_store(store: Annotated[StoreBase, Body()], session: SessionDep) -> Store:
    return crud.create_store(store, session)


@store_router.put('/{store_id}')
async def update_store(store_id: Annotated[int, Path(gt=0)], store: Annotated[StoreUpdate, Body()], session: SessionDep) -> Store:
    return crud.update_store(store_id, store, session)


@store_router.delete('/{store_id}')
async def delete_store(store_id: Annotated[int, Path(gt=0)], session: SessionDep) -> dict:
    if not crud.delete_store(store_id, session):
        return {'result': 'False'}
    return {'result': 'ok'}

router.include_router(category_router)
router.include_router(store_router)
