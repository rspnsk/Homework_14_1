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

    def add_product(self, product: Product) -> None:
        """Добавить товар в категорию."""
        if isinstance(product, Product):
            self.__products.append(product)
            # При добавлении нового товара увеличиваем общий счетчик
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    @property
    def products(self) -> str:
        """Геттер для вывода списка товаров в нужном формате"""
        products_list = [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
                         for product in self.__products]
        return "\n".join(products_list)
