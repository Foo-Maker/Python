# Die if Abfrage berücksichtigt boolean Werte. Entweder ist etwas wahr oder falsch.
# 
# Aufbau:     if VARIABLE: 
#
# Der Doppelpunkt gehört zur Syntax und muss direckt hintes der Variable stehen.

is_male = False

if is_male:                             #Wenn is_male wahr ist, dann wird print ausgeführt. Wenn nicht wird es übersprungen
    print("Du bist Mänlich")


if is_male:                             #Wenn is_male wahr ist, dann
    print("Du bist Mänlich")
else:                                   #Sonst…
    print("Du bist nicht Mänlich")


is_tall = True

if is_male or is_tall:                  #Wenn eins der beiden Werte (oder beide) wahr ist/sind, dann 
    print("Du bist Mänlich oder groß oder beides")
else:
    print("Du bist weder Mänlich noch groß")


if is_male and is_tall:                  #Wenn beide Werte wahr sind, dann  (eins alleine reicht nicht)
    print("Du bist Mänlich und groß")
else:
    print("Du bist kein großes mänliches Wesen")

if is_male and is_tall:                  #Wenn beide Werte wahr sind, dann  (eins alleine reicht nicht)
    print("Du bist Mänlich und groß")
elif not(is_male) and is_tall:           #Durch not() wird der wert in das Gegenteil verkehrt (True wird False und andersrum)
    print("Du bist eine große Frau")
elif (is_male) and not(is_tall):
    print("Du bist ein kleiner Mann")
else:
    print("Du bist einu kleine Frau")


# Man muss ja nicht direck ein boolean rein werfen. Es ist auch möglich mit hilfe von Operatoren die zu erzeugen.
# Im folgenden Codeschnipsel vergleichen wir Werte und geben den größten wieder aus.

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

nu1 = input("Bitte die erste Zahl eingeben.: ")
nu2 = input("Bitte die zwiete Zahl eingeben.: ")
nu3 = input("Bitte die dritte Zahl eingeben.: ")

print("Die größte Zahl war " + str(max_num(float(nu1), float(nu2), float(nu3))))

# Auch andere Variablentypen können verglichen werden. Hier ein Beispiel von Strings

if "Otto" == input("Wie heißt Du? "):
    print("Du bist Otto.")
else:
    print("Du bist nicht Otto!")