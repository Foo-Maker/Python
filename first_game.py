secret_wort = "Hubertus"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != secret_wort and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Bitte das Wort eingeben.: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Alle Versuche verbraucht. Da hast Verloren.")
else:
    print("Glückwunsch! Das geheime Wort war " + guess)