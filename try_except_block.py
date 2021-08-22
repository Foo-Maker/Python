'''
Damit das Programm bei Fehlern nicht Abbricht, sollte man den try and except Block nutzen.
In try wird geschaut ob etwas durch läuft. Ist dem nicht so, dann werden die except-Blöcke abgerufen.

Im Beispiel ist das erste except für eine Nulldivision. Da mann nichts durch 0 teilen kann würde normal hier das Programm abbrechen.

In diesen Fall jedoch sagen wir das es hier einen Fehler gibt.
'''
import random                           # Wird benötigt für einen zufallswert

try:
    wert = 10/ random.randint(0, 1)     # Mit random.randint(0, 1) erzeugen wir eine zufällige Zahl zwischen 0 und 1 für die Division
    number = int(input("Bitte eine Zahl eingeben: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
    print("Wie bitte? Das ist Mathematisch nicht lösbar!")
except ValueError:
    print("Das geht nicht. Ich kann nur mit ganzen Zahlen umgehen.")