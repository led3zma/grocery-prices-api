from sqlmodel import Field, SQLModel


class Category(SQLModel, table=True):
    __tablename__ = "categories"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)


class Store(SQLModel, table=True):
    __tablename__ = "stores"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)


class Product(SQLModel, table=True):
    __tablename__ = "products"

    id: int | None = Field(default=None, primary_key=True)
    description: str
    added_by: str | None = Field(default=None)
    category_id: int | None = Field(default=None, foreign_key="categories.id")


class Price(SQLModel, table=True):
    __tablename__ = "prices"

    id: int | None = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="products.id")
    store_id: int = Field(foreign_key="stores.id")
    currency: int = Field(gt=0)
    price: float = Field(ge=0)
    rate: float = Field(ge=0)
    added_by: str | None = Field(default=None)
