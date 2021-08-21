for letter in "Eine kleine for Schleife":
    print(letter)

freunde = ["Tim", "Mike","Anton", "Georg", "Hugo"]
for freund in freunde:
    print(freund)

for index in range(3, 10):
    print(index)

for index in range(len(freunde)):
    print(index)
    print(freunde[index])

for index in range(len(freunde)):
    if index == 3:
        print("Der vierte Name")
    else:
        print("Nicht der vierte Name")
    print(freunde[index])