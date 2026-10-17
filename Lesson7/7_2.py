import unittest


class TestNumbersList(unittest.TestCase):
    def setUp(self):
        print("Preparating the list")
        self.numbers = [1,2,3,4,5]
    def tearDown(self):
        print("Remowing numbers")
    def test_list_has_five_numbers(self):
        self.assertEqual(len(self.numbers), 5)
    def test_list_has_four_numbers(self):
        self.assertIn(4, self.numbers)


