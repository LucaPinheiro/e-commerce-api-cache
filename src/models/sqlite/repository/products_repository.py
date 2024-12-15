from .interfaces.products_repository import ProductRepositoryInterface
from sqlite3 import Connection as SqliteConnection
from typing import Tuple


class ProductRepository(ProductRepositoryInterface):
    def __init__(self, conn: SqliteConnection) -> None:
        self.__conn = conn

    def find_product_by_name(self, product_name: str) -> tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            'SELECT * FROM products WHERE name = ?',
            (product_name,)
        )
        return cursor.fetchone()

    def insert_product(self, name: str, price: float, quantity: int) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            'INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)',
            (name, price, quantity)
        )
        self.__conn.commit()