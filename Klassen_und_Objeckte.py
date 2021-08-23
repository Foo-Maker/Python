'''
    Wir kennen ja verschiedene Typen von Datentypen. (Strings, Integer, Float, Boolean, …)
    Doch was ist wenn wir eine eigene Art von Datentypen haben wollen?
    (Person, Tier, Auto, Matal, …)
    Dann müssen wir diesen Typ erstellen und geht in Python über Klassen.

    Erstellen wir also mal eine Klasse…

    (Die kann natürlich auch über den importdialog wie eine Funktion eingebunden werden.
    from Datei import Klasse  [ from Klassen_und_Objeckte import Schüler ] )
'''

class Schüler:
    def __init__(self, name, alter, ist_mänlich):
        self.name = name
        self.alter = alter
        self.ist_mänlich = ist_mänlich

'''
    Mit class haben wir die Klasse definiert und anschließend wurde durch def __init__(self) mitgegeben was noch für Werte in diese Klasse gehören.
    self.name = name übergeben wir dem Wert Name den inhalt der Variable name. 
    Zu self. gibt es nachher mehr…
'''

Schüler1 = Schüler("Uwe", 13, True)

#   Dadurch das wir einer Variable (Schüler1) mit Daten der Klasse >Schüler< gefüllt haben, ist der Schüler1 ein Objekt.

print(Schüler1.name)

#   wir können natürlich auch die Werte in einem Objekt ändern.

print(Schüler1.alter)
Schüler1.alter = 44
print(Schüler1.alter)

#   Was passiert nun wenn ich einfach nur Schüler 1 ausgeben lasse?

print(Schüler1)

'''
    Wie wir sehen steht da Folgendes…
    <__main__.Schüler object at 0x7fba0b1d1fd0>
    Doch was genau bedeutet dies? 
    Hier wird ausgegeben das Schüler1 eine Objekt ist und im Arbeitsspeicher unter der Adresse 0x7fba0b1d1fd0 zu finden ist.
    Dies nennt man auch eine Referenz weil das Objekt "nur" auf eine Stelle referenziert.

    Genau aus diesem Grund muss auch das self Parameter benutzt werden wenn wir eine Klasse definieren!
    Wenn wir nämlich ein Objekt erstellen wollen, dann geht Python hin und referenziert ein Teil der Arbeitspeichers der dann mit Attributen gefüllt wird.
    Darum wird self angegeben da an der stelle der aktuell eigene Speicherbereich genutzt werden soll.
'''
