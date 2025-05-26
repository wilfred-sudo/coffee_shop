from order import Order
from coffee import Coffee

class Customer:
    def __init__(self, name: str):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = value

    def orders(self):
        return [order for order in Order.all_orders() if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee: Coffee, price: float):
        if not isinstance(coffee, Coffee):
            raise TypeError("create_order expects a Coffee instance.")
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee: Coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("most_aficionado expects a Coffee instance.")
        # Calculate total spent per customer on this coffee
        spending = {}
        for order in Order.all_orders():
            if order.coffee == coffee:
                spending[order.customer] = spending.get(order.customer, 0) + order.price
        if not spending:
            return None
        # Return customer with max spending
        return max(spending, key=spending.get)