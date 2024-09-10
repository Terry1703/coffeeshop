import unittest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("David")
        self.coffee = Coffee("Mocha")
        self.order = Order(self.customer, self.coffee, 4.0)

    def test_order_initialization(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.coffee, self.coffee)
        self.assertEqual(self.order.price, 4.0)

if __name__ == "__main__":
    unittest.main()
