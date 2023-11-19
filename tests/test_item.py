"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item


def test_item():
    item1 = Item("Камера", 10000, 25)
    Item.pay_rate = 0.8
    assert item1.calculate_total_price() == 8000
    item1.apply_discount()
    assert item1.price == 7500
    assert Item.all == ["Камера", 7500, 25]
