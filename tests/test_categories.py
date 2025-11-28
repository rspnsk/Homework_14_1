import pytest
from src.categories import Category
from src.products import Product


def test_category_init() -> None:
    # Тест 1: Создание категории без товаров
    category1 = Category("Электроника", "Электронные устройства")
    assert category1.name == "Электроника"
    assert category1.description == "Электронные устройства"
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_init_with_products(category1):
    # Проверка, что при создании категории атрибуты инициализировались корректно
    assert category1.name == "Электроника"
    assert category1.description == "Электронные устройства"
    assert len(category1._Category__products) == 1  # Проверка приватного атрибута


# Тест добавления товара в категорию
def test_add_product(category1, apple_product):
    # Создадим новый продукт
    product2 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    category1.add_product(product2)

    # Проверим, что продукт успешно добавлен
    assert len(category1._Category__products) == 2
    assert category1._Category__products[-1] == product2


# Тест на невозможность добавления объекта, не являющегося Product
def test_add_product_invalid_type(category1):
    # Проверим, что нельзя добавить объект, не являющийся Product
    with pytest.raises(TypeError):
        category1.add_product("Некорректный объект")


# Тест геттера для вывода списка товаров
def test_products_property(category1):
    # Проверим геттер для вывода списка товаров
    expected_output = "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert category1.products == expected_output


# Тест глобальных счётчиков категорий и товаров
def test_class_attributes(category1):
    # Проверим, что при создании и добавлении товаров обновляются общие счётчики
    assert Category.category_count == 1
    assert Category.product_count == 1

    # Добавим ещё один товар
    category1.add_product(Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5))
    assert Category.product_count == 2
