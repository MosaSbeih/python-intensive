"""
module.py contains functions that generate random products and calculate their average price
"""
import random
import itertools


from functools import reduce
from dataclasses import dataclass
from enum import IntEnum
from typing import Generator, Union


class Vegetable(IntEnum):
    """
    The enumeration of available Vegetables
    """
    Tomato = 1
    Potato = 2
    Cucumber = 3
    Pumpkin = 4
    Corn = 5


class Drinks(IntEnum):
    """
    The enumeration of available Vegetables Drinks
    """
    Soda = 1
    Water = 2
    Juice = 3


PRICE_RANGE = (0.10, 2.15)
PRODUCTS = (Vegetable, Drinks)


@dataclass
class Product:
    """
    A data class representing a product

    Attributes:
    ----------
    product_id : int -> (Product id for a specific category)

    product_type : Any -> (Vegetables, Drinks, etc...)

    product_price : int
        """
    product_id: int
    product_type: Union[Vegetable, Drinks]
    product_price: float

    def __lt__(self, other):
        return self.product_type < other.product_type


def product_avg_price(products: Generator) -> Generator[tuple, None, None]:
    """
    Function that calculates the average price of different products

    Parameters:
    ----------
    products: Product -> (sequence of Products)

    Return:
    ------
    Generator[tuple] -> Generator[(product_type, avg), ('Tomato', 1.12), etc...]
    """

    def avg(list_to_reduce):
        return reduce(lambda a, b: a + b, list_to_reduce) / len(list_to_reduce)

    groups = itertools.groupby(sorted(products), key=lambda product: product.product_type)
    for key, sub_group in groups:
        yield key, round(avg([product.product_price for product in sub_group]), 2)


def generate_products(quantity: int) -> Generator[Product, None, None]:
    """
    Function that generates random products

    Parameters:
    ----------
    quantity: int

    Return:
    ------
    Generator[Product]
    """
    for _ in range(quantity + 1):
        product_category = random.choice(PRODUCTS)
        product_type = random.choice(list(product_category.__members__.values()))
        product_price = random.uniform(PRICE_RANGE[0], PRICE_RANGE[1])

        yield Product(product_type.value, product_type.name, product_price)
