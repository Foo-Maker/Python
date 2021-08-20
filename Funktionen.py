# Funktionen werden erstellt in dem man erstmal   def   eintippt. Damit sagt man Python das eine Funktion definiert wird.
# Danach kommt der Name der Funktion. Wie bei Variablen sollte der Name aussagekräftig sein.
# Dann (): 
#
# Danach kommt der Code dar Funktion. Dieser muss passend eingerückt sein. Die Funktion endet durch das nicht mehr eingerückte.

def say_hi ():
    print("Hallo User")

# Um die Funktion aufzurufen schreiben wir einfach den Namen gefolgt von ()
# In diesen Beispiel say_hi()

print("Oben")
say_hi()
print("Unten")

# Natürlich kann man einer Funktion auch Parameter übergeben.
# Machen wir es also etwas komplexer

def greet_user(name, alter):
    print("Hallo " + name + ", du bist also " + alter + "Jahre alt.") 

greet_user(input("Bitte Namen angeben.: "), input("Wie alt bist denn du? "))

# Wie wir hier sehen habe ich in der Definition angegeben das ich zwei Werte übergeben möchte.
# Die abfrage der Werte habe ich direkt in den Aufruf gelegt. Sicher hätte man den Umweg über Variable machen können,
# allerdings geht es so schneller. (Das andere wäre nur für die Lesbarkeit schöner gewesen)



def cube(num):
    return num*num*num  #Durch return wird hier der Wert an print zurück gegeben.
                        #Ohne return würde das Ergebniss zwar ausgerechnet, aber an nichts übergeben.
    print("Durch den return Befehl wird die Funktion beendet. Dieser Text wird nicht wiedergegeben!")   # Ohne Funktion durch den return Befehl
    
print(cube(4))