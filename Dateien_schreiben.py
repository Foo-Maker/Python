'''
Grundlagen sind in Dateien_lesen.py 
'''
from datetime import datetime                   #Zur Veranschaulichung ist es schön einen Zeitstempel zu nehmen. Dann sieht man das es geht

testfile = open("Test.txt", "a")                #Wir öffnen die Datei mit den rechten etwas anzuhängen
                                                #Wenn wir w für write nehmen würden, dann würden wir den gesamten Inhalt überschreiben

testfile.write(str(datetime.now()) + "\n")      #Wir fügen der Datei Test.txt den Zeitstempel hinzu und fügen einen Zeilenumbruch an

testfile.close()                                #Schließt die Datei