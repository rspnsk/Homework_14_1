import pytest
from src.categories import Category
from src.products import Product


# fixture для Класс-метода new_product, который принимает на вход параметры товара в словаре
# и возвращает созданный объект класса Product
@pytest.fixture
def product_dict():
    return {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8}


# Определение фикстуры для проверки правильности работы геттера и сеттера
@pytest.fixture
def apple_product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


# Фикстура для создания другого продукта
@pytest.fixture
def samsung_product():
    return Product("Samsung Galaxy S23 Ultra", "Samsung Galaxy S23 Ultra", 180000.0, 5)


# Фикстура для категории
@pytest.fixture
def category1(apple_product):
    return Category("Электроника", "Электронные устройства", [apple_product])


# Фикстура для сброса счётчиков перед каждым тестом
@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0


# Фикстура для создания товаров
@pytest.fixture
def product_fixtures():
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    ]


# Фикстура для создания категории в class Category
@pytest.fixture
def category(product_fixtures):
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    )
    for product in product_fixtures:
        category.add_product(product)
    return category
