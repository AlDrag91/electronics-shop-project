"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


def test_item():
    item1 = Item("Камера", 10000, 25)
    Item.pay_rate = 0.8
    assert item1.calculate_total_price() == 8000
    item1.apply_discount()
    assert item1.price == 7500
    assert Item.all == ["Камера", 7500, 25]
    #  Test геттер и сеттер
    item1.name = "Электролампа"
    assert item1.name == 'Электролам'

    #  Тест четение файла и подсчет данных
    Item.instantiate_from_csv('../src/itemss.csv')
    assert len(Item.all) == 5
    item1 = Item.all[0]

    assert item1.name == 'Смартфон'

    #  возвращение числа из числа-строки
    assert Item.string_to_number('55.5') == 55
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('5.5') == 5

    #  __repr__ и __str__
    item1 = Item("флэш-память", 500, 5)
    assert repr(item1) == "Item('флэш-память', 500, 5)"
    assert str(item1) == 'флэш-память'
