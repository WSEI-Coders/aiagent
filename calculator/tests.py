import unittest
from pkg.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Ta metoda uruchamia się przed każdym testem.
        # Tworzymy tu nowy "świeży" obiekt kalkulatora.
        self.calculator = Calculator()

    # 🔹 Poniżej masz listę testów do zaimplementowania.
    #    Każdy opis mówi dokładnie:
    #    - jakie wyrażenie wywołać,
    #    - jaki powinien być wynik,
    #    - jakiego rodzaju asercji użyć.

    def test_addition(self):
        """Wyrażenie '3 + 5' powinno zwrócić 8."""
        # TODO:
        # 1. Wywołaj self.calculator.evaluate("3 + 5")
        # 2. Sprawdź za pomocą self.assertEqual(...), że wynik == 8
        self.fail("Not implemented")

    def test_subtraction(self):
        """Wyrażenie '10 - 4' powinno zwrócić 6."""
        # TODO: analogicznie jak wyżej, ale dla odejmowania
        self.fail("Not implemented")

    def test_multiplication(self):
        """Wyrażenie '3 * 4' powinno zwrócić 12."""
        # TODO: test mnożenia
        self.fail("Not implemented")

    def test_division(self):
        """Wyrażenie '10 / 2' powinno zwrócić 5."""
        # TODO: test dzielenia
        self.fail("Not implemented")

    def test_nested_expression(self):
        """Wyrażenie '3 * 4 + 5' powinno zwrócić 17.

        Uwaga: tu sprawdzamy, czy działa poprawna kolejność działań:
        najpierw 3 * 4 = 12, potem 12 + 5 = 17.
        """
        # TODO: sprawdź, że evaluate("3 * 4 + 5") zwraca 17
        self.fail("Not implemented")

    def test_complex_expression(self):
        """Wyrażenie '2 * 3 - 8 / 2 + 5' powinno zwrócić 7.

        Rozpiska:
        - 2 * 3 = 6
        - 8 / 2 = 4
        - 6 - 4 + 5 = 7
        """
        # TODO: sprawdź, że wynik jest równy 7
        self.fail("Not implemented")

    def test_empty_expression(self):
        """Puste wyrażenie ('') powinno zwrócić None.

        Metoda evaluate() ma zwrócić None, jeśli wyrażenie jest puste
        lub zawiera tylko białe znaki.
        """
        # TODO:
        # - wywołaj evaluate("") lub np. evaluate("   ")
        # - użyj self.assertIsNone(...)
        self.fail("Not implemented")

    def test_invalid_operator(self):
        """Wyrażenie z nieprawidłowym operatorem powinno rzucić ValueError.

        Przykład:
        - evaluate("$ 3 5")
        powinno zakończyć się rzuceniem ValueError (invalid token).
        """
        # TODO:
        # - użyj konstrukcji with self.assertRaises(ValueError):
        #       self.calculator.evaluate("$ 3 5")
        self.fail("Not implemented")

    def test_not_enough_operands(self):
        """Wyrażenie z za małą liczbą operandów powinno rzucić ValueError.

        Przykład:
        - evaluate("+ 3")
        nie ma dwóch liczb do działania, więc powinien polecieć ValueError
        (not enough operands for operator ...).
        """
        # TODO:
        # - użyj again self.assertRaises(ValueError) dla takiego wyrażenia
        self.fail("Not implemented")


if __name__ == "__main__":
    # Dzięki temu plik można uruchomić bezpośrednio:
    #   uv run calculator/tests.py
    unittest.main()
