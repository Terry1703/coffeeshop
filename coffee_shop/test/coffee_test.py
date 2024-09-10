import unittest
from coffee_shop.coffee import Coffee
from coffee_shop.customer import Customer
from coffee_shop.order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.coffee = Coffee("Espresso")
        self.customer = Customer("Charlie")
        self.order1 = self.customer.create_order(self.coffee, 2.5)
        self.order2 = self.customer.create_order(self.coffee, 3.0)

    def test_coffee_name(self):
        self.assertEqual(self.coffee.name, "Espresso")

    def test_num_orders(self):
        self.assertEqual(self.coffee.num_orders(), 2)

    def test_average_price(self):
        self.assertEqual(self.coffee.average_price(), 2.75)

if __name__ == "__main__":
    unittest.main()
