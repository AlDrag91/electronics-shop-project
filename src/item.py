import csv


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
        self.all.append(self)

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

        self.price *= self.pay_rate

        self.all.extend([self.__name, self.price, self.quantity])

    @property
    def name(self):
        return f'{self.__name}'

    @name.setter
    def name(self, __name):
        """Длину наименования товара оставляет 10 симвовов"""
        self.__name = __name[:10]

    @classmethod
    def instantiate_from_csv(cls, file):
        """Инициализирующий экземпляры класса `Item` данными из файла"""
        cls.all = []
        """Логику метода оборачиваем в try/except"""
        try:
            with open(file, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=",")
                for row in reader:
                    cls.all.append(Item(row['name'], row['price'], row['quantity']))
        except FileNotFoundError:
            # raise FileNotFoundError("Отсутствует файл item.csv")
            print("Отсутствует файл item.csv")
        except KeyError:
            raise InstantiateCSVError
        else:
            print("Файл в порядке продолжаю работу!")

    @staticmethod
    def string_to_number(number):
        return int(float(number))

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        return self.quantity + other.quantity


class InstantiateCSVError(Exception):
    """Класс исключения Поврежденный файл"""

    def __init__(self, *args):
        self.message = args[0] if args else 'Файл item.csv поврежден.'

    def __str__(self):
        return 'Файл item.csv поврежден.'  # f"{self.message}"
