monthConversions = {
    "Jan" : "January",
    "Feb" : "Februar",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}                                                       # Legt Schlüssel für Werte fest

print(monthConversions["Feb"])                          # Hier wird der Wert für den Schlüssel Feb ausgegeben
#print(monthConversions["tie"])                         # Hier wird ein Fehler ausgegeben weil es den Wert nicht gibt
print(monthConversions.get("tie", "Ungültiger Wert"))   # Durch get können wir bei ungültigen Werten einen andere Ausgabe abrufen