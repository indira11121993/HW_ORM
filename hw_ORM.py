import sqlalchemy
import sqlalchemy as sq

from sqlalchemy import create_engine, Table, MetaData, Column, BIGINT, String, Integer, FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DSN = "postgresql://postgres:Umar2011@localhost:5432/hwormdb"
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    name = sq.Column(sq.String(length=50), unique=True)

    def __str__(self):
        return f'id издателя - {self.id}: Имя издателя - {self.name}'


class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    title = sq.Column(sq.String(length=50), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="book")

    def __str__(self):
        return f'{self.id}: {self.title}'



class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    name = sq.Column(sq.String(length=30), unique=True)

    def __str__(self):
        return f'{self.id}:{self.name}'


class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=True)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")

    def __str__(self):
        return f'{self.id}:{self.count}'


class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    price = sq.Column(sq.NUMERIC, nullable=False)
    date_sale = sq.Column(sq.DateTime, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref="sale")

    def __str__(self):
        return f'{self.id}:{self.price}, {self.date_sale}, {self.count}'

def create_tables(engine):
    Base.metadata.create_all(engine)

create_tables(engine)


session.close()