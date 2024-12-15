from src.http_types.http_request import HttpRequest
from src.http_types.http_resposnse import HttpResponse
from src.models.repository.interfaces.redis_repository_interface import RedisRepositoryInterface
from src.models.sqlite.repository.interfaces.products_repository import ProductRepositoryInterface


class ProductFinder:
    def __init__(self, redis_repo: RedisRepositoryInterface, products_repo: ProductRepositoryInterface) -> None:
        self.__redis_repo = redis_repo
        self.__products_repo = products_repo

    def find_by_name(self, http_request: HttpRequest) -> HttpResponse:
        product_name = http_request.params.get('name')

