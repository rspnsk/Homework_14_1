from typing import Optional
from src.products import Product


class Category:
    # Атрибуты класса для хранения общей информации
    category_count = 0  # Общее количество категорий
    product_count = 0  # Общее количество товаров во всех категориях

    def __init__(self, name: str, description: str, products: Optional[list[Product]] = None):
        """
        Класс для представления категории товаров.
        :param name: название категории
        :param description: описание категории
        :param products: список товаров в категории (по умолчанию пустой)
        """
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        # Увеличиваем счетчик категорий при создании новой категории
        Category.category_count += 1
        # Учитываем количество товаров в новой категории
        Category.product_count += len(self.__products)

    def __str__(self):
        quantity_sum = 0
        for product in self.__products:
            quantity_sum += product.quantity
        return f"{self.name}, количество продуктов: {quantity_sum} шт."

    def add_product(self, product: Product) -> None:
        """Добавить товар в категорию."""
        if isinstance(product, Product):
            self.__products.append(product)
            # При добавлении нового товара увеличиваем общий счетчик
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    def middle_price(self):
        """Метод, который подсчитывает средний ценник всех товаров, и
        когда в категории нет товаров и сумма всех товаров будет делиться на ноль,
        возвращает ноль."""
        try:
            total_price = sum(product.price for product in self.__products)
            average_price = total_price / len(self.__products)
            return average_price
        except ZeroDivisionError:
            return 0

    @property
    def products(self) -> list[Product]:
        """Геттер для получения списка товаров, что бы работать с этими объектами напрямую,
        а не с их строковым представлением."""
        return self.__products


class CategoryIterator:
    """ Класс для итерации продуктов одной категории. Принимает на вход объект класса Category
    и производит итерацию по товарам, которые хранятся в данной категории."""
    def __init__(self, category: Category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.products):
            result = self.category.products[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
