import csv

from icecream import ic


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
         :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.pay_rate
        price = total_price
        return price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price - (self.price * self.quantity / 100)

        self.all.extend([self.__name, self.price, self.quantity])

    @property
    def name(self):
        return f'{self.__name}'

    @name.setter
    def name(self, __name):
        """длину наименования товара оставляет 10 симвовов"""
        self.__name = __name[:10]

    @classmethod
    def instantiate_from_csv(cls, file):
        """инициализирующий экземпляры класса `Item` данными из файла"""
        cls.all = []
        with open(file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",")
            for row in reader:
                # name = row['name']
                # price = int(row['price'])
                # quantity = int(row['quantity'])
                ic(row)
                cls.all.append(Item(row['name'], row['price'], row['quantity']))
                #cls(name, price, quantity)

    @staticmethod
    def string_to_number(number):
        return int(float(number))

