import pytest
from src.order import Order


# Тестирование конструктора класса Order
def test_order(apple_product):
    order = Order(apple_product, 2)
    assert order.product == apple_product
    assert order.quantity == 2
    assert order.total_cost == 420000.0


# Тестирование метода __str__
def test_order_str(apple_product):
    order = Order(apple_product, 3)
    expected_str = 'Iphone 15 3 630000.0'
    assert str(order) == expected_str


# Тест на передачу не Product объекта
def test_non_product_argument():
    with pytest.raises(AttributeError):
        Order("Некорректный объект", 2)
