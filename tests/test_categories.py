import pytest
from src.categories import Category, CategoryIterator
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


# # Тест геттера для вывода списка товаров
# def test_products_property(category1):
#     # Проверим геттер для вывода списка товаров
#     expected_output = "Iphone 15, 210000.0 руб. Остаток: 8 шт."
#     assert category1.products == expected_output


# Тест глобальных счётчиков категорий и товаров
def test_class_attributes(category1):
    # Проверим, что при создании и добавлении товаров обновляются общие счётчики
    assert Category.category_count == 1
    assert Category.product_count == 1

    # Добавим ещё один товар
    category1.add_product(Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5))
    assert Category.product_count == 2


# К ДЗ 15.1
# Тест успешного обхода товаров
def test_iterator_successfully_iterate(category):
    iterator = CategoryIterator(category)
    products = list(iterator)
    assert len(products) == 3
    assert products[0].name == "Samsung Galaxy S23 Ultra"
    assert products[1].name == "Iphone 15"
    assert products[2].name == "Xiaomi Redmi Note 11"


# Тест останова итерации после последнего элемента
def test_stop_iteration(category):
    iterator = CategoryIterator(category)
    # Перебираем все товары
    for _ in range(len(category.products)):
        next(iterator)
    # Следующий вызов должен вызвать StopIteration
    with pytest.raises(StopIteration):
        next(iterator)


# Тест пустой категории
def test_empty_category():
    empty_category = Category("Телевизоры", "чтобы смотреть")
    iterator = CategoryIterator(empty_category)
    # Категория пустая, итерация должна закончиться немедленно
    with pytest.raises(StopIteration):
        next(iterator)


# Тест проверка работы метода метод __str__ для class Category
def test_str_category(category):
    assert str(category) == "Смартфоны, количество продуктов: 27 шт."


# Тест проверка работы метода метод __str__ для class Product
def test_str_product(apple_product):
    assert str(apple_product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


# Тест геттера products
def test_products_getter(category1, apple_product):
    # Проверяем, что геттер возвращает корректный список товаров
    products = category1.products
    assert isinstance(products, list)
    assert len(products) == 1
    assert products[0] == apple_product


# Тест среднего значения цены, при наличии товаров
def test_middle_price_with_products(fruits_category):
    # Средняя цена: (210000.0 + 180000.0) / 2 = 195000.0
    result = fruits_category.middle_price()
    assert result == 195000.0


# Тест среднего значения при отсутствии товаров
def test_middle_price_without_products(empty_category):
    result = empty_category.middle_price()
    assert result == 0
