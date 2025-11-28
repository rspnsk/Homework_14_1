

class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Класс для представления товара.
        :param name: название товара
        :param description: описание товара
        :param price: цена товара (может содержать дробную часть)
        :param quantity: количество товара в наличии
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict):
        """
        Класс-метод, который принимает на вход параметры товара в словаре и возвращает созданный объект класса Product
        """
        name = product_dict["name"]
        description = product_dict["description"]
        price = product_dict["price"]
        quantity = product_dict["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """ Геттер для получения цены товара. """
        return self.__price

    @property
    def products(self):
        """ Геттер для вывода списка товаров в нужном формате """
        return f'{self.name}, {self.__price} руб.Остаток: {self.quantity} шт.'

    @price.setter
    def price(self, new_price):
        """ Сеттер для реализации проверки цены"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price >= self.__price:
            self.__price = new_price
        else:
            access = input("Подтвердите цену: y = да, n = нет: ")
            if access == "y":
                self.__price = new_price
            else:
                print("Изменение цены отменено")
