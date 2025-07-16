# main_app.py

# TODO 5: Importiere die Funktion 'say_hello' aus dem Modul 'greetings'.
from greetings import say_hello



# TODO 6: Importiere die Funktion 'add' aus dem Modul 'math_utils'.
from math_utils import add

if __name__ == "__main__":
    print("Willkommen zu deiner eigenen Modul-Anwendung!")

    # TODO 7: Rufe say_hello mit deinem Namen auf und gib das Ergebnis aus.
    say_hello("Andreas")
    # TODO 8: Rufe add mit zwei Zahlen auf und gib das Ergebnis aus.
    print(add(2, 3))
    