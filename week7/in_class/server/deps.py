from typing import Callable
from redis import Redis
from server.triton import TritonClient


def get_redis() -> Redis | None:
    ...


def get_triton() -> Callable[[str], TritonClient | None]:
    ...
