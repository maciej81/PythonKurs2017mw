# sprawdz czy liczba jest podzielna przez 3, 5, 7

liczba = input("podaj liczbe: ")

if liczba.isnumeric():
    #instrukcje
    liczba = int(liczba)

    if liczba % 3 == 0:
        print("liczba jest podzielna przez 3")

    if liczba % 5 == 0:
        print("liczba jest podzielna przez 5")

    if liczba % 7 == 0:
        print("liczba jest podzielna przez 7")
else:
    print("podaj tylko liczbe")