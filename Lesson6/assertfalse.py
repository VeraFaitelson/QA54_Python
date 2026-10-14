from unittest import TestCase, main


# === 1. Рабочая функция ===
def is_even(num):
    return num % 2 == 0


# === 2. Класс с тестами ===
class TestMathFunctions(TestCase):

    # Тест из прошлого примера (на чётность)
    def test_check_even(self):
        # Ожидаем True, так как 4 — чётное
        self.assertTrue(is_even(4))

    # НАШ НОВЫЙ ТЕСТ: проверка нечётного числа
    def test_check_odd(self):
        # Функция is_even(5) вернёт False (так как 5 не делится на 2 без остатка).
        # Метод assertFalse поймает этот False и скажет: "Всё правильно, это число НЕ чётное!"
        self.assertFalse(is_even(5))


if __name__ == "__main__":
    main()