#Eine Liste ist ein Array. In diesen Array können wir allerdings mehrere Reihen anlegen.
#Anhand diese Beispiels habe ich pro Reihe ein zusätzliches Array angelegt.

gitter = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#Wenn wir nun ein ein bestimmten Wert aufrufen möchten, dann geben wir erst die Reihe an unt die Spalte.

print(gitter[2][1])     # array[Reihe][Spalte]

#zur Ausgabe der einzelnen Reihen reicht eine einfache for-Schleife

for row in gitter:
    print(row)

#Natürlich kann man auch aus jeder Reihe die einzelne Spalte ausgeben
for row in gitter:
    for col in row:
        print(col)
