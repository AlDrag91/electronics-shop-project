
from src.keyboard import Keyboard


def test_keyboard():
    kb = Keyboard('Keyboard 7030', 1500, 50)
    # Проверка названия товара
    assert str(kb) == 'Keyboard 7030'
    print("-------->")
    print(kb)

    # Проверка стандартной раскладки клавиатуры
    assert str(kb.language) == "EN"
    print(kb.language)

    # Изменение раскладки клавиатуры
    kb.change_lang()
    assert str(kb.language) == "RU"
    print(kb.language)

    # Обратное изменение раскладки клавиатуры
    kb.change_lang()
    assert str(kb.language) == "EN"
    print(kb.language)
