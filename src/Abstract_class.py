from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс - родитель для класса продуктов"""
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        pass


class BaseCategory(ABC):
    """Абстрактный класс - родитель для класса категорий"""
    def __init__(self, name: str):
        self.name = name


class MixinPrint:
    """Класс-миксин для печати в консоль информации в читаемом виде"""
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        """Метод для информативного отображения и отладки"""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
