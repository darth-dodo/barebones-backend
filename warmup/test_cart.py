from unittest import TestCase
from cart import Product, ShoppingCart


class TestShoppingCart(TestCase):
    def _create_product(self):
        test_product = Product
        test_product.name = "Dummy Product"
        test_product.quantity = 4
        test_product.price = 10.5

        return test_product

    def setUp(self):
        self.cart = ShoppingCart(max_size=200)

    def test_add_element_to_cart(self):
        product = self._create_product()
        self.cart.add_product(product)
        assert self.cart.price == product.price * product.quantity
        assert len(self.cart) == product.quantity

    def test_add_same_element_twice(self):
        product = self._create_product()

        self.cart.add_product(product)
        self.cart.add_product(product)

        assert self.cart.price == (product.price * product.quantity * 2)
        assert len(self.cart) == (product.quantity * 2)

    def test_add_two_different_elements(self):

        product_1 = Product
        product_1.name = "Product 1"
        product_1.price = 10
        product_1.quantity = 2

        product_2 = Product
        product_2.name = "Product 2"
        product_2.price = 5
        product_2.quantity = 2

        self.cart.add_product(product_1)
        self.cart.add_product(product_2)

        assert self.cart.price == (
            (product_1.price * product_1.quantity)
            + (product_2.price * product_2.quantity)
        )
        assert len(self.cart) == product_1.quantity + product_2.quantity
