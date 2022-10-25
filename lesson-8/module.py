"""
module.py contains functions that generate random products and calculate their average price
"""
import random


from dataclasses import dataclass
from enum import IntEnum


class Vegetable(IntEnum):
    """
    Vegetables!
    """
    Tomato = 1
    Potato = 2
    Cucumber = 3
    Pumpkin = 4
    Corn = 5


class Drinks(IntEnum):
    """
    Drinks!
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

    ...

    Attributes:
    ----------
    product_id : int
        Product id for a specific category
    product_type : Any
        Vegetables, Drinks, etc...
    product_price : int
        """
    product_id: int
    product_type: Vegetable
    product_price: float


# returns [('Tomato', 1.12), ('Juice', 1.05), etc...]
def product_avg_price(sequence: iter) -> list[tuple]:
    """
    Function that calculates the average price of different products

    ...

    Parameters:
    ----------
    sequence: Product
        A sequence of Products

    Return:
    ------
    list[tuple]
    """
    product_data = {}
    for data in sequence:
        key = data.product_type.__str__()
        if key in product_data:
            product_data[key] = (product_data[key][0] + data.product_price, product_data[key][1] + 1)
        else:
            product_data[key] = product_data.get(key, (data.product_price, 1))

    for items in product_data.items():
        product_data[items[0]] = round(items[1][0]/items[1][1], 2)

    return list(product_data.items())


def generate_products(items_range: int):
    """
    Function that generates random products

    ...

    Parameters:
    ----------
    items_range: int
        How many products do you want?

    Return:
    ------
    generator
    """
    for _ in range(items_range + 1):
        product_category = random.choice(PRODUCTS)
        product_type = random.choice(list(product_category.__members__.values()))
        product_price = random.uniform(PRICE_RANGE[0], PRICE_RANGE[1])

        yield Product(product_type.value, product_type.name, product_price)
