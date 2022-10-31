from sqlalchemy import (
    ForeignKey,
    Identity,
    Column,
    String,
    Integer,
    Text,
    create_engine,
)
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    sessionmaker,
    relationship,
    with_expression,
    query_expression,
)


engine = create_engine("postgresql://postgres:postgres@localhost:5432/my_shop")

if not database_exists(engine.url):
    create_database(engine.url)

base = declarative_base()


class Category(base):
    __tablename__ = "category"

    c_id = Column(Integer, Identity(start=1, cycle=True), primary_key=True)
    c_name = Column(String(100), nullable=False)
    description = Column(Text)


class Discount(base):
    __tablename__ = "discount"

    d_id = Column(Integer, Identity(start=1, cycle=True), primary_key=True)
    d_name = Column(String(100), nullable=False)
    percent = Column(Integer)


class Product(base):
    __tablename__ = "product"

    p_id = Column(Integer, Identity(start=1, cycle=True), primary_key=True)
    p_name = Column(String(100), nullable=False)
    p_price = Column(Integer, nullable=False)
    c_id = Column(Integer, ForeignKey("category.c_id", ondelete="CASCADE"))
    category = relationship("Category", backref="products")
    d_id = Column(Integer, ForeignKey("discount.d_id", ondelete="CASCADE"))
    discount = relationship("Discount", backref="products")
    pretty_price = query_expression()


base.metadata.create_all(engine)


category_stuff = [
    Category(c_name="Fruts", description="we all can eat it"),
    Category(c_name="Shoes", description="no high hills"),
    Category(c_name="Shampo", description="no parabens"),
    Category(c_name="Vegetables", description="fermer's product"),
]

discount_stuff = [
    Discount(d_name="Black", percent=35),
    Discount(d_name="Birthday", percent=12),
    Discount(d_name="Extrem", percent=50),
    Discount(d_name="First", percent=15),
]


product_stuff = [
    Product(p_name="Apples", p_price=12, c_id=1, d_id=1),
    Product(p_name="Snikers", p_price=200, c_id=2, d_id=2),
    Product(p_name="Pantine", p_price=23, c_id=3, d_id=3),
    Product(p_name="Tomatoes", p_price=10, c_id=4, d_id=4),
]


Session = sessionmaker(engine)

with Session() as session:
    session.add_all(category_stuff)
    session.add_all(discount_stuff)
    session.add_all(product_stuff)
    session.commit()


min_price = int(input("Set a min price for range: "))
max_price = int(input("Set a max price for range: "))


with Session() as session:
    result = (
        session.query(Product)
        .options(
            with_expression(
                Product.pretty_price,
                Product.p_price - Product.p_price * Discount.percent / 100,
            )
        )
        .join(Product.category)
        .join(Product.discount)
        .filter(Product.p_price.between(min_price, max_price))
    )
    for row in result:
        print(
            row.p_id,
            row.p_name,
            row.p_price,
            row.category.c_name,
            row.category.description,
            row.discount.d_name,
            row.discount.percent,
            row.pretty_price,
        )
