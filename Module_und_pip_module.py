'''
    Diese Datei ist nur zur Veranschaulichung von Modulen gedacht.
    Damit so etwas anständig läuft sollte die Datei nur aus Funktionen bestehen.
'''

def say_hi ():
    print("Hallo User")

def greet_user(name, alter):
    print("Hallo " + name + ", du bist also " + alter + " Jahre alt.") 

def cube(num):
    return num*num*num  #Durch return wird hier der Wert an print zurück gegeben.
                        #Ohne return würde das Ergebniss zwar ausgerechnet, aber an nichts übergeben.
    print("Durch den return Befehl wird die Funktion beendet. Dieser Text wird nicht wiedergegeben!")   # Ohne Funktion durch den return Befehl
