from typing import NamedTuple
import logging

logger = logging.getLogger(__name__)


class Product(NamedTuple):
    name: str
    price: float
    quantity: int


class ShoppingCart:
    """
from cart import ShoppingCart, Product

product_1 = Product(name="Product 1", price=10.5, quantity=4)
cart = ShoppingCart()

print(len(cart))
print(cart.price)
print(str(cart))

cart.add_product(product_1)

cart.add_product(product_1)

cart

print(len(cart))
print(cart.price)
print(str(cart))


product_2 = Product(name="Product 2", price=5, quantity=3)
    """

    def __init__(self, max_size: int = 20):
        self._max_size = max_size
        self._elements = dict()
        self._total_price = 0
        self._total_quantity = 0

    def add_product(self, product: Product):

        if self._is_filled(product):
            raise ValueError("Cannot add more elements to the cart")

        existing_product = self._elements.get(product.name)

        if existing_product:
            existing_product["quantity"] = (
                existing_product.get("quantity") + product.quantity
            )
            self._elements[product.name] = existing_product
        else:
            new_product = dict()
            new_product["quantity"] = product.quantity
            new_product["price"] = product.price
            new_product["name"] = product.name
            self._elements[product.name] = new_product

        self._update_cart_total_price(product)
        self._update_cart_total_elements(product)

        print(
            f"Successfully added Product {product.name} with {product.quantity} in the cart!"
        )

    @property
    def price(self):
        return self._total_price

    def _update_cart_total_elements(self, product: Product):
        self._total_quantity += product.quantity

    def _update_cart_total_price(self, product: Product):
        self._total_price += product.quantity * product.price

    def _is_filled(self, product: Product):
        new_quantity = self._total_quantity + product.quantity
        logger.debug(
            f"Current quantity is {self._total_quantity} and new quantity will be {new_quantity}"
        )
        return new_quantity >= self._max_size

    def __str__(self):
        return f"Cart Stats:\n\t- Unique Elements: {len(self._elements.keys())}\n\t- All Elements: {len(self)}\n\t- Total Price: {self.price} "

    def __repr__(self):
        return f"Cart Stats:\n\t- Unique Elements: {len(self._elements.keys())}\n\t- All Elements: {len(self)}\n\t- Total Price: {self.price} "

    def __len__(self):
        return self._total_quantity
