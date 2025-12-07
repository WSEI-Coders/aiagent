import sys
from pkg.calculator import Calculator
from pkg.render import format_json_output


def main():
    # Tworzymy obiekt kalkulatora, który zna zasady liczenia wyrażeń.
    calculator = Calculator()

    # sys.argv to lista argumentów podanych w linii komend.
    # sys.argv[0] -> nazwa pliku (np. "main.py")
    # sys.argv[1:] -> reszta, czyli to, co wpisze użytkownik
    #
    # Jeśli użytkownik nie poda żadnego argumentu (czyli długość listy <= 1),
    # to wyświetlamy prostą instrukcję i kończymy program.
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    # Jeśli argumenty są podane, składamy je w jedno wyrażenie.
    # Przykład:
    #   python main.py 3 + 5
    # sys.argv[1:] = ["3", "+", "5"]
    # " ".join(...) -> "3 + 5"
    expression = " ".join(sys.argv[1:])

    try:
        # Próbujemy policzyć wynik wyrażenia za pomocą kalkulatora.
        result = calculator.evaluate(expression)

        # Jeśli wynik nie jest None, tzn. wyrażenie nie było puste
        if result is not None:
            # format_json_output tworzy ładny tekst w formacie JSON,
            # zawierający zarówno wyrażenie, jak i wynik.
            to_print = format_json_output(expression, result)
            print(to_print)
        else:
            # evaluate() zwraca None, gdy wyrażenie jest puste
            # lub zawiera tylko białe znaki (spacje, taby itd.)
            print("Error: Expression is empty or contains only whitespace.")
    except Exception as e:
        # Jeśli w trakcie obliczeń coś pójdzie nie tak (np. zły operator),
        # łapiemy wyjątek i wypisujemy komunikat błędu.
        #
        # Uwaga: tu łapiemy ogólny Exception – w testach można będzie
        # sprawdzić konkretne typy błędów rzucane w Calculator.evaluate().
        print(f"Error: {e}")


# Ten blok sprawia, że funkcja main() odpala się tylko wtedy,
# gdy plik jest uruchomiony bezpośrednio:
#   python main.py
# a NIE wtedy, gdy ktoś importuje ten moduł w innym pliku.
if __name__ == "__main__":
    main()
