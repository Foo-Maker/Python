'''
Mit open kann man Dateien öffnen. Jeh nach modus gibt man hier bestimmte rechte auf die Datei.

    readme = open("Dateien_lesen.py", "r")

Mit dem Befehl öffnen wir genau diese Datei hier im "nur lese Modus"
Wenn wir bei , "r") das r austauschen gibt es Folgende Möglichkeiten.

r  = read               leserechte
w  = write              schreibrechte !!!!! ACHTUNG !!!!! vorhandener inhalt wird überschrieben
a  = append             Der Datei etwas anfügen
r+ = read and write     lese und schreiberechte

Im Anschluss sollte die Datei immer geschlossen werden.
'''

readme = open("Dateien_lesen.py", "r")      #Wir öffnen die Datei
print(readme.readable())                    #ist die Datei lesbar
#print(readme.read())                       #gibt die Datei aus
#print(readme.readline())                   #gibt die erste Zeile aus
#print(readme.readline())                   #und die folgende
#print(readme.readline())                   #…
#print(readme.readlines())                  #Gibt alles als Array aus
#print(readme.readlines()[3])               #Da es ein Array ist kann man auch entsprechend damit umgehen

count = 1
for i in readme.readlines():
    print("Zeile " + str(count) + " : " + i)
    count+=1

readme.close()                              #Schließt die Datei