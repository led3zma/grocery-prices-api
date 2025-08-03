from sqlmodel import Field, SQLModel

# Category Models


class CategoryBase(SQLModel):
    name: str = Field(index=True)


class Category(CategoryBase, table=True):
    __tablename__ = "categories"

    id: int | None = Field(default=None, primary_key=True)


class CategoryUpdate(CategoryBase):
    name: str | None = None

# Store Models


class StoreBase(SQLModel):
    name: str = Field(index=True)


class Store(StoreBase, table=True):
    __tablename__ = "stores"

    id: int | None = Field(default=None, primary_key=True)


class StoreUpdate(StoreBase):
    name: str | None = None

# Product Models


class ProductBase(SQLModel):
    description: str
    added_by: str | None = Field(default=None)
    category_id: int | None = Field(default=None, gt=0)


class Product(ProductBase, table=True):
    __tablename__ = "products"

    id: int | None = Field(default=None, primary_key=True)
    category_id: int | None = Field(default=None, foreign_key="categories.id")


class ProductUpdate(ProductBase):
    description: str | None = None
    added_by: str | None = None
    category_id: int | None = None


# Price Models

class PriceBase(SQLModel):
    product_id: int = Field(gt=0)
    store_id: int = Field(gt=0)
    currency: int = Field(gt=0)
    price: float = Field(ge=0)
    rate: float = Field(ge=0)
    added_by: str | None = Field(default=None)


class Price(PriceBase, table=True):
    __tablename__ = "prices"

    id: int | None = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="products.id")
    store_id: int = Field(foreign_key="stores.id")


class PriceUpdate(PriceBase):
    product_id: int | None = Field(default=None, gt=0)
    store_id: int | None = Field(default=None, gt=0)
    currency: int | None = Field(default=None, gt=0)
    price: float | None = Field(default=None, ge=0)
    rate: float | None = Field(default=None, ge=0)
    added_by: str | None = None
