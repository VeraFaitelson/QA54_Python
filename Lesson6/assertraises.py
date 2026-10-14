from unittest import TestCase, main


# Функция, которую мы тестируем
def divide(a, b):
    return a / b


class TestCalculator(TestCase):

    def test_divide_by_zero(self):
        # 1. Открываем контекст и указываем, КАКУЮ ошибку ждём
        with self.assertRaises(ZeroDivisionError):
            # 2. Вызываем ломающийся код
            divide(10, 0)

        # Если ошибка произошла, мы успешно выходим из блока with.
        # Тест горит ЗЕЛЁНЫМ!


if __name__ == "__main__":
    main()