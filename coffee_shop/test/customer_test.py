import unittest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")
        self.order = self.customer.create_order(self.coffee, 3.5)

    def test_create_customer(self):
        self.assertEqual(self.customer.name, "Alice")

    def test_create_order(self):
        self.assertIn(self.order, self.customer.orders())

    def test_create_order_invalid_price(self):
        with self.assertRaises(ValueError):
            self.customer.create_order(self.coffee, 10.5)

    def test_most_aficionado(self):
        customer2 = Customer("Bob")
        customer2.create_order(self.coffee, 5.0)
        self.assertEqual(Customer.most_aficionado(self.coffee), customer2)

if __name__ == "__main__":
    unittest.main()
