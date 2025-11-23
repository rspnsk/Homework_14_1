from src.categories import Product


def test_init() -> None:
    """Тест проверки корректности инициализации объекта"""
    product = Product(
        name="Смартфон", description="Современный смартфон с большим экраном", price=29999.99, quantity=10
    )

    # Проверяем, что все атрибуты установлены правильно
    assert product.name == "Смартфон"
    assert product.description == "Современный смартфон с большим экраном"
    assert product.price == 29999.99
    assert product.quantity == 10


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
    """ тест проверки создания нового экземпляра из словаря"""
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
