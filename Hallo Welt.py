#Strings
 
print("Hallo Welt ich lerne Python!")
foo = "Jetzt brauche ich mal schnell einen einfachen Text."
print(foo)
print(foo[23])  #Giebt die 23te Stelle an. Startet mit 0
print(len(foo)) #len steht für length unt gibt an wieviele Stellen die Variable hat. Startet mit 0
print(foo.replace("t", "i"))
print(foo.replace("t", "itie"))

#Nunbers

print(24)
print(24.2354234)
print(-34.2423)
print(24 + 245)
print(24 - 23)
print(24 / 2)
print(24 * 2.4)
print(24 + 2 * 2)
print((24 + 2) * 2)
print(10 % 3)   # Gibt den Rest aus nach der 3er potenz. (3,6,9… zu 10 bleibt noch 1 über)
print(2**64)    #Gibt das Ergebniss von > 2 hoch 64 < aus

my_num = 4
my_num_neg = -2

print(my_num)
print(my_num + 2)
print(str(my_num))                  # Hier wird aus dem Matthematischen Wert ein String generiet
print(str(my_num) + " ist toll")    # Hier funktioniert die Ausgabe weil die Zahl auch ein String ist. Man kann verschiedene Typen nicht mischen.
print(f"{my_num} ist toll")         # Auch eine Möglichkeit zur ausgabe… (f steht für format. Es formatiert die Ausgabe)
#print(my_num + " ist toll")        # Wirft einen Fehler aus weil hier unterschiedliche Datentypen genutzt wurden.
print(my_num + -1)
print(abs(my_num_neg))              # Gibt den absoluten Wert aus. Aus -2 wird 2
print(pow(4, 6))                    # Gibt an wie oft ein Wert mit sich selbst Multipliziert wirt. Hier 4 hoch 6, bzw 4*4*4*4*4*4
print(max(4, 6))                    # Gibt an was der höchste numerische Wert ist. 
print(min(4, 6))                    # Gibt an was der nidrigste numerische Wert ist. 
print(round(4.67))                  # Werte ab-, aufrunden

from math import *  # importiert alles von "math" (Matthe Bibliothek)

print(floor(3.81))  # Rundet immer ab
print(ceil(3.81))   # Rundet immer auf
print(sqrt(36))     # Zieht die Quadratwurzel

