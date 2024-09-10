from .order import Order
from .coffee import Coffee

class Customer:
    customers = []

    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = name
        Customer.customers.append(self)

    @property
    
    def name(self):
        return self._name

    @name.setter
    
    def name(self, value):
        
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = value

    def orders(self):
        return [order for order in Order.orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        
        if not isinstance(coffee, Coffee):
            raise ValueError("Argument must be a Coffee instance.")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        return Order(self, coffee, price)

    @classmethod
    
    
    def most_aficionado(cls, coffee):
        
        if not isinstance(coffee, Coffee):
            raise ValueError("Argument must be a Coffee instance.")
        customers = [customer for customer in cls.customers if coffee in customer.coffees()]
        if not customers:
            return None
        return max(customers, key=lambda c: sum(o.price for o in c.orders() if o.coffee == coffee))

