freunde = ["Tim", "Mike","Anton", "Georg", "Hugo"]
#           0      1      2        3        4 
#Bei der Auflistung beginnt man das Zählen bei 0
#Es ist allesdings auch möglich rückwerts zu zählen.
#Dann wäre der erste Wert -1 (Hugo).
#-2 Georg -3 Anton

print(freunde[2])

#Außerdem ist es möglich einen Bereich anzugeben

print(freunde[1:3]) #Der erste Wert gibt an wo gestartet wird. Der Zweite welche Position die erste ist die nicht mehr gezeigt wird.
print(freunde[2:])  #So wird alles ab "2" angezeigt
print(freunde[-2:]) #Die erste Position ist -2 und ab da geht es weiter nach hinten
print(freunde[:2])  #Von Anfang an bis zu dem ersten Wert der nicht mehr angezeigt wird
# Der Syntax ist also [von:bis_nicht_mehr]

#Es ist aber auch möglich Werte zu verändern.
print(freunde[2:5])
freunde[3] = "Olaf"
print(freunde[2:5])
freunde.append("Christian") #Hängt den Wert an das Ende der Liste
print(freunde)
freunde.insert(2, "Jan")    #Fügt den Wert an die Stelle 2 (Nicht vergessen. Wir fangen das Zählen bei 0 an.) Der Rest wird nach rechts verschoben.
print(freunde)
freunde.remove("Jan")
print(freunde)
#freunde.clear() #Löscht die Liste
#print(freunde)
freunde.pop()   #Löscht den letzten in der Liste
print(freunde)
print(freunde.index("Hugo"))    #Zeigt an, an welchen Stelle der Wert in der Liste steht.
print(freunde.count("Tim"))     #Zählt wie oft ein Wert in der Liste steht.

zahlen = [2, 124, 7, 23, 456, 64]

print(zahlen)
zahlen.sort()   #Sotiert die Liste
print(zahlen)
zahlen.reverse()    #Sortiert absteigend
print(zahlen)

freunde2 = freunde.copy()   #kopiert den Inhalt von freunde nach freunde2
print(freunde2)
freunde2.extend(zahlen)     #Fügt die Liste zahlen an freunde2 an
print(freunde2)