from src.item import Item


class Phone(Item):
    """Дочерний класс от класса Item"""

    def __init__(self, name, price, quantity, number_of_sim):
        """Инициализируем кол-во сим-карт и вызываем метод класса-родителя"""

        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __add__(self, other):
        """Магический метод сложения и логика проверки принадлежности к классу-родителя"""
        if not isinstance(other, Item):
            return "ValueError('Складывать можно только объекты Item и дочерние от них.')"
        return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        """Проверка на кол-во сим-карт"""
        if int(number) <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim = number
