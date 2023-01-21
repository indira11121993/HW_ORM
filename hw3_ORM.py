import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from hw_ORM import create_tables, Publisher, Shop, Book, Stock, Sale


DSN = "postgresql://postgres:Umar2011@localhost:5432/hwormdb"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('jsonf.json', 'r') as jf:
    data = json.load(jf)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()

session.close()