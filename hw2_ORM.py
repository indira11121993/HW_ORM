import sqlalchemy
from sqlalchemy.orm import sessionmaker

from hw_ORM import create_tables, Publisher, Shop, Book, Stock, Sale

DSN = "postgresql://postgres:Umar2011@localhost:5432/hwormdb"
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

for p in session.query(Publisher).all():
    print(p)

id_pub = input("Введите id издателя : ")
id_pub = int(id_pub)

result_query = session.query(
    Sale
).join(
    Stock, Stock.id == Sale.id_stock
).join(
    Shop, Shop.id == Stock.id_shop
).join(
    Book, Book.id == Stock.id_book
).join(
    Publisher, Publisher.id == Book.id_publisher
)
for sale in result_query.filter(Publisher.id == id_pub):
    print(f"{sale.stock.book.title} | {sale.stock.shop.name} | {sale.price} | {sale.date_sale}")




