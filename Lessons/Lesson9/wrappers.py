"""
Decorators / wrappers
"""
import random
from typing import Callable


def check_floats(func: Callable[[float, float], float]) -> Callable[[float, float], float]:
    def wrapper(a: float, b: float) -> float:
        # before function call
        assert type(a) == float
        assert type(b) == float
        return_value: float = func(a, b)
        # after function call
        assert type(return_value) == float
        return return_value

    return wrapper


def square(func: Callable[[float, float], float]) -> Callable[[float, float], float]:
    def wrapper(a: float, b: float) -> float:
        return func(a ** 2, b ** 2)

    return wrapper


@check_floats
def add(a: float, b: float) -> float:
    # DRY - Don't repeat yourself
    return a + b


@square
@check_floats
def subtract(a: float, b: float) -> float:
    return a - b


def test_add():
    a = float(random.randint(-10000, 10000))
    b = float(random.randint(-10000, 10000))
    assert add(a, b) == a + b


test_add()
# print(check_types(add)(5., 7.))
print(add(7., 3.))
print(subtract(3., 2.))
