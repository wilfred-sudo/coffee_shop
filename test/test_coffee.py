import pytest
from .test_coffee import Coffee
from .test_customer import Customer

def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("ab")
    c = Coffee("Mocha")
    assert c.name == "Mocha"

def test_num_orders_and_average_price():
    coffee = Coffee("Espresso")
    customer = Customer("Eve")
    customer.create_order(coffee, 3.0)
    customer.create_order(coffee, 4.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 3.5