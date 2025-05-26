import pytest
from .test_customer import Customer
from .test_coffee import Coffee

def test_customer_name_validation():
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("a" * 16)
    c = Customer("Alice")
    assert c.name == "Alice"

def test_create_order():
    c = Customer("Bob")
    coffee = Coffee("Latte")
    order = c.create_order(coffee, 4.5)
    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 4.5