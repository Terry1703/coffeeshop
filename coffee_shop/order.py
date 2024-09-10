class Order:
    orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer) or not isinstance(coffee):
            raise ValueError("Invalid Customer or Coffee instance.")
        if not isinstance(price, (int, float)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
