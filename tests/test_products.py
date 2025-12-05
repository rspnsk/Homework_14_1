from src.categories import Product
from src.products import Smartphone, LawnGrass


def test_init() -> None:
    """Тест проверки корректности инициализации объекта класса Product"""
    product = Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )

    # Проверяем, что все атрибуты установлены правильно
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_init_Smartphone() -> None:
    """Тест проверки корректности инициализации объекта класса Smartphone"""
    product_Smartphone = Smartphone(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5,
        efficiency=95.5, model="S23 Ultra", memory=256, color="Серый"
    )

    # Проверяем, что все атрибуты установлены правильно
    assert product_Smartphone.name == "Samsung Galaxy S23 Ultra"
    assert product_Smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert product_Smartphone.price == 180000.0
    assert product_Smartphone.quantity == 5
    assert product_Smartphone.efficiency == 95.5
    assert product_Smartphone.model == "S23 Ultra"
    assert product_Smartphone.memory == 256
    assert product_Smartphone.color == "Серый"


def test_init_LawnGrass() -> None:
    """Тест проверки корректности инициализации объекта класса LawnGrass"""
    product_LawnGrass = LawnGrass(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5,
        country="Россия", germination_period="7 дней", color="Зеленый"
    )

    # Проверяем, что все атрибуты установлены правильно
    assert product_LawnGrass.name == "Samsung Galaxy S23 Ultra"
    assert product_LawnGrass.description == "256GB, Серый цвет, 200MP камера"
    assert product_LawnGrass.price == 180000.0
    assert product_LawnGrass.quantity == 5
    assert product_LawnGrass.country == "Россия"
    assert product_LawnGrass.germination_period == "7 дней"
    assert product_LawnGrass.color == "Зеленый"


def test_init_types() -> None:
    """Тест проверки типов данных при инициализации"""
    product = Product(
        name="Смартфон", description="Современный смартфон с большим экраном", price=29999.99, quantity=10
    )

    # Проверяем типы данных атрибутов
    assert isinstance(product.name, str), "Имя должно быть строкой"
    assert isinstance(product.description, str), "Описание должно быть строкой"
    assert isinstance(product.price, float), "Цена должна быть float"
    assert isinstance(product.quantity, int), "Количество должно быть целым числом"


def test_new_product(product_dict):
    """ Тест проверки создания нового экземпляра из словаря"""
    assert Product.new_product(product_dict).name == "Iphone 15"
    assert Product.new_product(product_dict).description == "512GB, Gray space"
    assert Product.new_product(product_dict).price == 210000.0
    assert Product.new_product(product_dict).quantity == 8


# Тестирование геттера и сеттера
def test_price_getter_and_setter(apple_product):
    # Проверка первоначального значения цены
    assert apple_product.price == 210000.0

    # Установим новое значение цены
    apple_product.price = 220000.0

    # Проверим, что цена успешно обновилась
    assert apple_product.price == 220000.0

    # Попробуем установить некорректную цену (например, отрицательное значение)
    apple_product.price = -10.0

    # Проверим, что цена осталась старой после неудачной попытки изменения
    assert apple_product.price == 220000.0
