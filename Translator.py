#ein kleines Programm bei dem wir Vokale durch G's ersetzen

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":           #durch das .lower() wird jeder Buchstabe als kleingeschrieben bewertet
            if letter.isupper():                #durch des .isupper() wird geguckt ob der Buchstabe groß geschrieben war
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Bitte den Text eingeben.: ")))