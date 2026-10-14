from unittest import TestCase, main


# === 1. Рабочая функция ===
# Проверяет, чётное ли число. Если чётное, возвращает True, если нет — False
def is_even(num):
    return num % 2 == 0


# === 2. Класс с тестами ===
class TestMathFunctions(TestCase):

    def test_check_even(self):
        # Метод assertTrue(X) проверяет, что внутри скобок (X) получилось True.
        # Так как 4 — чётное число, функция is_even(4) вернёт True. Тест пройдёт!
        self.assertTrue(is_even(4))

    def test_check_examples_from_image(self):
        # А это примеры из комментариев вверху картинки:
        # assertEqual сравнивает два значения между собой
        self.assertEqual(2 + 2, 4)


if __name__ == "__main__":
    main()