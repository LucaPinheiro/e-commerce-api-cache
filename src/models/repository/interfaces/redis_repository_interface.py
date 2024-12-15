from abc import abstractmethod

from redis import Redis

class RedisRepositoryInterface:

    @abstractmethod
    def __init__(self, redis_conn: Redis) -> None:
        pass

    @abstractmethod
    def insert(self, key: str, value: any) -> None:
        pass

    @abstractmethod
    def get_key(self, key: str) -> str:
        pass

    @abstractmethod
    def insert_hash(self, key: str, field: str, value: any) -> None:
        pass

    @abstractmethod
    def get_hash(self, key: str, field: str) -> any:
        pass

    @abstractmethod
    def insert_ex(self, key: str, value: any, ex: int) -> None:
        pass

    @abstractmethod
    def insert_hash_ex(self, key: str, field: str, value: any, ex: int) -> None:
        pass