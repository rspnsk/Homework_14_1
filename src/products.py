

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

    def __str__(self):
        """ Магический метод __str__, который возвращает строку:
        Название продукта, X руб. Остаток: X шт."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """ Магический метод сложения __add__, который принимает два аргумента: self и второй объект.
        Метод возвращает сумму произведений цены на количество у двух объектов."""
        if isinstance(other, Product):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise TypeError("Нельзя складывать объект Product с объектом другого типа.")

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
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

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


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """ Магический метод сложения __add__, который принимает два аргумента: self и второй объект.
        Метод возвращает сумму произведений цены на количество у двух объектов."""
        if type(other) is Smartphone:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError("Нельзя складывать объект Smartphone с объектом другого типа.")


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """ Магический метод сложения __add__, который принимает два аргумента: self и второй объект.
        Метод возвращает сумму произведений цены на количество у двух объектов."""
        if type(other) is LawnGrass:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError("Нельзя складывать объект LawnGrass с объектом другого типа.")
