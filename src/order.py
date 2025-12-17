from src.products import Product


class Order:
    def __init__(self, product: Product, quantity: int):
        """
        Класс Заказ, в котором хранится информация о покупке товара.
        :param product: объект класса Product, представляющий приобретённый товар
        :param quantity: количество приобретённого товара
        """
        self.product = product  # Хранит объект класса Product
        self.quantity = quantity
        self.total_cost = product.price * quantity

    def __str__(self):
        return f"__str__ {self.product.name} {self.quantity} {self.total_cost}"

# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     Order1 = Order(product1, 2)
#     print(Order1)
