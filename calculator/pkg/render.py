import json


def format_json_output(expression: str, result: float, indent: int = 2) -> str:
    """
    Funkcja pomocnicza do "ładnego" formatowania wyniku kalkulatora jako tekst JSON.

    Parametry:
    - expression: oryginalne wyrażenie w postaci stringa, np. "3 + 5"
    - result: wynik obliczeń (zazwyczaj float)
    - indent: ile spacji ma być użyte do wcięć w JSON-ie (domyślnie 2)

    Zwraca:
    - string w formacie JSON, np.:
      {
        "expression": "3 + 5",
        "result": 8
      }
    """

    # Jeśli wynik jest typu float, ale w rzeczywistości jest liczbą całkowitą
    # (np. 8.0, 10.0), to konwertujemy go na int, żeby w JSON-ie wyglądał ładniej:
    # "result": 8 zamiast "result": 8.0
    if isinstance(result, float) and result.is_integer():
        result_to_dump = int(result)
    else:
        # W przeciwnym wypadku zostawiamy wynik bez zmian (może być float albo inny typ).
        result_to_dump = result

    # Przygotowujemy słownik z danymi wyjściowymi.
    # Klucze to "expression" i "result", wartości to odpowiednio:
    # - oryginalny tekst wyrażenia,
    # - wynik obliczeń (po ewentualnej konwersji).
    output_data = {
        "expression": expression,
        "result": result_to_dump,
    }

    # json.dumps zamienia słownik w string z JSON-em.
    # Parametr indent=indent sprawia, że JSON jest sformatowany „ładnie”
    # (z nowymi liniami i wcięciami), a nie jako jedno długie zdanie.
    return json.dumps(output_data, indent=indent)
