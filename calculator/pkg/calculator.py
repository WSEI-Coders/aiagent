class Calculator:
    def __init__(self):
        # Słownik operatorów:
        #   klucz  -> symbol operatora w wyrażeniu (np. "+")
        #   wartość -> funkcja (lambda), która przyjmuje dwa argumenty a, b
        #              i zwraca wynik działania
        #
        # Dzięki temu nie musimy pisać wielkiego if/elif dla każdego operatora,
        # tylko wybieramy odpowiednią funkcję ze słownika.
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }

        # Precedencja operatorów – czyli "ważność" przy liczeniu.
        # Im wyższa liczba, tym operator ma wyższy priorytet.
        #
        # W matematyce mnożenie i dzielenie wykonujemy przed dodawaniem
        # i odejmowaniem – stąd 2 dla * i /, a 1 dla + i -.
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def evaluate(self, expression):
        """
        Główna metoda kalkulatora.
        Przyjmuje wyrażenie jako string, np. "3 * 4 + 5"
        i zwraca jego wynik jako liczbę (float).

        Zasady:
        - jeśli expression jest puste lub zawiera tylko spacje -> zwracamy None
        - w przeciwnym razie:
          * rozbijamy string na tokeny (po spacjach),
          * przekazujemy listę tokenów do metody _evaluate_infix().
        """
        # Jeśli expression to pusty string ("") lub same białe znaki (np. "   "),
        # nie ma czego liczyć, więc zwracamy None.
        if not expression or expression.isspace():
            return None

        # Usuwamy nadmiarowe spacje na końcach i dzielimy po pojedynczych
        # odstępach. Np. " 3  +  5 " -> ["3", "+", "5"]
        tokens = expression.strip().split()

        # Liczenie właściwe odbywa się w osobnej metodzie,
        # która zakłada, że dostaje listę tokenów (napisów).
        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens):
        """
        Implementacja prostego parsera/obliczacza wyrażeń w notacji infiksowej.

        Przykładowe wyrażenie:
            "3 * 4 + 5"
        po podziale na tokeny:
            ["3", "*", "4", "+", "5"]

        Używamy dwóch stosów:
        - values    -> przechowuje liczby
        - operators -> przechowuje operatory (+, -, *, /)

        Algorytm działa tak:
        1. Przechodzimy po tokenach jeden po drugim.
        2. Jeśli token jest operatorem:
           - sprawdzamy precedencję względem ostatniego operatora na stosie,
           - jeśli poprzedni operator ma wyższą lub równą ważność,
             to go "aplikujemy" (czyli liczymy fragment wyrażenia),
           - na końcu wrzucamy bieżący operator na stos.
        3. Jeśli token NIE jest operatorem:
           - próbujemy zrzutować go na float (liczbę),
           - jeśli się nie da -> rzucamy ValueError (zły token).
        4. Po przejściu całej listy tokenów:
           - stos operators może nadal zawierać operatory,
             więc stosujemy je aż do końca.
        5. Na końcu na stosie values powinna zostać dokładnie jedna liczba –
           to jest wynik. Jeśli nie, to znaczy, że wyrażenie było niepoprawne.
        """
        values = []     # stos liczb
        operators = []  # stos operatorów (+, -, *, /)

        for token in tokens:
            # Przypadek 1: token jest jednym z dozwolonych operatorów
            if token in self.operators:
                # Dopóki:
                # - na stosie operatorów coś jest
                # - ostatni operator jest znanym operatorem
                # - i ma wyższy lub równy priorytet niż bieżący token
                # to stosujemy (liczymy) ten operator.
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)

                # Po zakończeniu pętli możemy spokojnie dołożyć
                # bieżący operator na stos.
                operators.append(token)

            else:
                # Przypadek 2: token powinien być liczbą.
                # Próbujemy zamienić tekst na float, np. "3" -> 3.0, "2.5" -> 2.5
                try:
                    values.append(float(token))
                except ValueError:
                    # Jeśli się nie uda (np. token="$"), to wyrażenie jest niepoprawne.
                    # Rzucamy ValueError z informacją, który token jest nieprawidłowy.
                    raise ValueError(f"invalid token: {token}")

        # Po przejściu wszystkich tokenów mogą nam jeszcze zostać
        # jakieś operatory na stosie – musimy je po kolei "zastosować".
        while operators:
            self._apply_operator(operators, values)

        # Na końcu powinna zostać dokładnie jedna wartość.
        # Jeśli jest inaczej, wyrażenie było zbudowane niepoprawnie,
        # np. brakowało liczby albo operatora.
        if len(values) != 1:
            raise ValueError("invalid expression")

        # Zwracamy jedyny element ze stosu – to wynik całego wyrażenia.
        return values[0]

    def _apply_operator(self, operators, values):
        """
        Pomocnicza metoda, która:
        - zdejmuje jeden operator ze stosu operatorów,
        - zdejmuje dwie liczby ze stosu wartości,
        - oblicza wynik operatora dla tych liczb,
        - wrzuca wynik z powrotem na stos wartości.

        Jeśli nie ma wystarczającej liczby operandów, rzuca ValueError.
        """
        # Jeśli na stosie operatorów nic nie ma, nie mamy co robić.
        if not operators:
            return

        # Bierzemy ostatni operator ze stosu (LIFO).
        operator = operators.pop()

        # Do poprawnego działania operatora binarnego (np. "a + b")
        # potrzebujemy DWÓCH wartości na stosie values.
        if len(values) < 2:
            # Jeśli jest ich mniej – sygnalizujemy błąd jasno po nazwie operatora.
            raise ValueError(f"not enough operands for operator {operator}")

        # Kolejność ma znaczenie:
        # najpierw ściągamy "b", potem "a" (stos działa jak stos talerzy).
        b = values.pop()
        a = values.pop()

        # W self.operators mamy zapisaną funkcję odpowiadającą danemu operatorowi.
        # Wywołujemy ją z argumentami a, b i wynik zapisujemy z powrotem.
        values.append(self.operators[operator](a, b))
