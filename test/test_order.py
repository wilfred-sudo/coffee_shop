import pytest
from .test_customer import Customer
from .test_coffee import Coffee
from .test_order import Order

def test_order_validation():
    customer = Customer("Dan")
    coffee = Coffee("Cappuccino")
    with pytest.raises(TypeError):
        Order("not_customer", coffee, 3.0)
    with pytest.raises(TypeError):
        Order(customer, "not_coffee", 3.0)
    with pytest.raises(TypeError):
        Order(customer, coffee, "not_price")
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0