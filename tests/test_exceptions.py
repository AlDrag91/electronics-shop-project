from src.item import Item


def test_missing_file():
    """Файл отсутствует"""
    try:
        Item.instantiate_from_csv("missing_file.csv")
    except Exception as ex:
        assert ex == 'Отсутствует файл item.csv'
        print(ex)


def test_defective_item():
    """Файл поврежден"""
    try:
        Item.instantiate_from_csv("../src/defective_item.csv")
    except Exception as ex:
        print(ex)


def test_correct_file():
    """Файл в порядке продолжаю работу!"""
    try:
        Item.instantiate_from_csv("../src/itemss.csv")
    except Exception as ex:
        print(ex)
