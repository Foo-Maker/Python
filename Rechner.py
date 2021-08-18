num1 = input("Erste Zahl: ")
num2 = input("Zweite Zahl: ")
#result = num1 + num2   #hier sind die Variablen noch Strings 
#print (result)         #Darum werden die hier hintereinander ausgegeben
result = float(num1) + float(num2)  #float macht hier aus dem string einen float (Fließkommazahl)
print (result)                      #Darum kann man hier mit Komma rechnen