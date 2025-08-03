from fastapi import HTTPException
from sqlmodel import Session, select
from app.models import Category, CategoryBase, CategoryUpdate, Store, StoreBase, StoreUpdate

# Category CRUD


def create_category(category: CategoryBase, session: Session) -> Category:
    category_db = Category.model_validate(category)
    session.add(category_db)
    session.commit()
    session.refresh(category_db)
    return category_db


def read_category(category_id: int, session: Session) -> Category | None:
    return session.get(Category, category_id)


def read_categories(session: Session) -> list[Category]:
    return session.exec(select(Category)).all()


def update_category(category_id: int, category: CategoryUpdate, session: Session) -> Category:
    category_db = read_category(category_id, session)
    if not category_db:
        raise HTTPException(status_code=404, detail="Category not found")
    category_db.sqlmodel_update(category.model_dump(exclude_unset=True))
    session.add(category_db)
    session.commit()
    session.refresh(category_db)
    return category_db


def delete_category(category_id: int, session: Session) -> bool:
    category_db = read_category(category_id, session)
    if not category_db:
        raise HTTPException(status_code=404, detail="Category not found")
    session.delete(category_db)
    session.commit()
    return True


# Store CRUD

def create_store(store: StoreBase, session: Session) -> Store:
    store_db = Store.model_validate(store)
    session.add(store_db)
    session.commit()
    session.refresh(store_db)
    return store_db


def read_store(store_id: int, session: Session) -> Store | None:
    return session.get(Store, store_id)


def read_stores(session: Session) -> list[Store]:
    return session.exec(select(Store)).all()


def update_store(store_id: int, store: StoreUpdate, session: Session) -> Store:
    store_db = read_store(store_id, session)
    if not store_db:
        raise HTTPException(status_code=404, detail="Store not found")
    store_db.sqlmodel_update(store.model_dump(exclude_unset=True))
    session.add(store_db)
    session.commit()
    session.refresh(store_db)
    return store_db


def delete_store(store_id: int, session: Session) -> bool:
    store_db = read_store(store_id, session)
    if not store_db:
        raise HTTPException(status_code=404, detail="Store not found")
    session.delete(store_db)
    session.commit()
    return True
