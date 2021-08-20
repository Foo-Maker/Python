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
    print("Da bist eine große Frau")
elif (is_male) and not(is_tall):
    print("Da bist ein kleiner Mann")
else:
    print("Du bist einu kleine Frau")