from src.item import Item

from src.phone import Phone


def test_phone():
    # __init__ и __repr__
    phone1 = Phone('Xiaomi POCO', 14543, 3, 2)
    assert phone1.name == 'Xiaomi POCO'
    print("--->>>>")
    print(phone1.name)
    assert phone1.price == 14543
    print(phone1.price)
    assert phone1.quantity == 3
    print(phone1.quantity)
    # __add__
    item1 = Item("Камера", 10000, 25)
    assert phone1 + item1 == 28
    print(phone1 + item1)
    # isinstance
    assert phone1 + 15 == "ValueError('Складывать можно только объекты Item и дочерние от них.')"
    print(phone1 + 15)
    # логика проверки отсутствий сим-карт ???
    phone1.number_of_sim = 0
