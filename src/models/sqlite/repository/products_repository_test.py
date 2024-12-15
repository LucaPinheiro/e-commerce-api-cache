from src.models.sqlite.settings.connection import SqliteConnectionHandle
from .products_repository import ProductRepository

conn_handle = SqliteConnectionHandle()
conn = conn_handle.connect()

def test_insert_products():
    repo = ProductRepository(conn)

    name = 'Alexa'
    price= 100.0
    quantity = 10

    repo.insert_product(name, price, quantity)