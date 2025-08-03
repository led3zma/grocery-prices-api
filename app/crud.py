from fastapi import HTTPException
from sqlmodel import Session, select
from app.models import Category, CategoryBase, CategoryUpdate, Price, PriceBase, PriceUpdate, Product, ProductBase, ProductUpdate, Store, StoreBase, StoreUpdate

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


# Product CRUD

def create_product(product: ProductBase, session: Session) -> Product:
    if not read_category(product.category_id, session):
        raise HTTPException(status_code=422, detail='Invalid category')
    product_db = Product.model_validate(product)
    session.add(product_db)
    session.commit()
    session.refresh(product_db)
    return product_db


def read_product(product_id: int, session: Session) -> Product | None:
    return session.get(Product, product_id)


def read_products(session: Session) -> list[Product]:
    return session.exec(select(Product)).all()


def update_product(product_id: int, product: ProductUpdate, session: Session) -> Product:
    product_db = read_product(product_id, session)
    if not product_db:
        raise HTTPException(status_code=404, detail="Product not found")
    product_db.sqlmodel_update(product.model_dump(exclude_unset=True))
    session.add(product_db)
    session.commit()
    session.refresh(product_db)
    return product_db


def delete_product(product_id: int, session: Session) -> bool:
    product_db = read_product(product_id, session)
    if not product_db:
        raise HTTPException(status_code=404, detail="Product not found")
    session.delete(product_db)
    session.commit()
    return True

# Price CRUD


def create_price(price: PriceBase, session: Session) -> Price:
    if not read_product(price.product_id, session):
        raise HTTPException(status_code=422, detail='Invalid product')
    if not read_store(price.store_id, session):
        raise HTTPException(status_code=422, detail='Invalid store')
    price_db = Price.model_validate(price)
    session.add(price_db)
    session.commit()
    session.refresh(price_db)
    return price_db


def read_price(price_id: int, session: Session) -> Price | None:
    return session.get(Price, price_id)


def read_prices(session: Session) -> list[Price]:
    return session.exec(select(Price)).all()


def update_price(price_id: int, price: PriceUpdate, session: Session) -> Price:
    price_db = read_price(price_id, session)
    if not price_db:
        raise HTTPException(status_code=404, detail="Price not found")
    price_db.sqlmodel_update(price.model_dump(exclude_unset=True))
    session.add(price_db)
    session.commit()
    session.refresh(price_db)
    return price_db


def delete_price(price_id: int, session: Session) -> bool:
    price_db = read_price(price_id, session)
    if not price_db:
        raise HTTPException(status_code=404, detail="Price not found")
    session.delete(price_db)
    session.commit()
    return True
