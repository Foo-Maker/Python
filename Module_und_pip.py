'''
    Module werden ebenso in Dateien gespeichert die mit .py enden.
    Wenn die Datei nun also geile_funktionen.py heißt, dann geht der Importdialog > import geile_funktionen <
    
    Der import Befehl importiert jedoch nicht nur die Funktionen, sondern alles.
    Aus diesem Grund ist es Empfehlenswert darauf zu achten, dass sich kein ungewollter Code einschleicht.

    Aufgerufen werden die Funktionen dann  >>>  geile_funktionen.wie_auch_immer_die_Funktion_heißt() <<<
    Ab da geht es wie gewohnt mit den Funktionen weiter…

'''

import Module_und_pip_module

Module_und_pip_module.say_hi()
print(Module_und_pip_module.cube(23))
Module_und_pip_module.greet_user(input("Name: "),str(input("Alter: ")))


'''
    Wenn man Funktionen benötigt die normal nicht vorhanden sind, dann kann man die in der Regel über pip installieren

    pip install gedoenz

    Es gibt auch einen uninstaller.

    pip uninstall gedoenz

    (gedoenz steht hier als Platzhalter…)
'''