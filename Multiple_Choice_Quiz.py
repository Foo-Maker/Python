#   Dies dient noch mal der Veranschaulichung von Objekten und Klassen anhand eines kleinen Multiple Choice Game

question_promts = [ #   Erstmal erstellen wir eine Liste von Fragen
    "Welche Farbe haben Äpfel? \n(a) Rot/Grün\n(b) Violett\n(c) Orange\n\n", 
    "Welche Farbe haben Bananen? \n(a) Blau\n(b) Magenta\n(c) Gelb\n\n", 
    "Welche Farbe haben Erdbeeren ? \n(a) Schwarz\n(b) Rot\n(c) Lila\n\n"
]

class Fragen:       #   Hier erstellen wir die Klasse. Zu erkennen an dem großen F bei Fragen
    def __init__(self, promt, answer):
        self.promt = promt
        self.answer = answer

fragen = [          #   Dies ist eine Liste die mit Objekten der Klasse Frage gefullt wird. (fragen klein geschrieben)
    Fragen(question_promts[0], "a"),
    Fragen(question_promts[1], "c"),
    Fragen(question_promts[2], "b")
]

def test(fragen):   #   Die Funktion test. Sie wird mit der Liste fragen gefüllt in der die Objekte liegen
    punkte = 0
    for frage in fragen: # frage (einzahl) ist das einzelne Objekt aus der Liste fragen
        antwort = input(frage.promt) # frage.promt ist die Frage des Objektes
        if antwort == frage.answer:  # frage.answer ist die Antwort des Objektes
            punkte += 1
    print("Du hast " + str(punkte) + " von " + str(len(fragen)))

test(fragen)        #   Aufruf der Funktion test mit übergabe der Liste fragen