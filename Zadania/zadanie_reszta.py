#wydaj reszte z zakupow

monety = [5, 2, 1, 0.5, 0.2, 0.1]
wydac = [0, 0, 0, 0, 0, 0]

banknot = 20
zakup = 11.3 #to sie wywali bo zaokraglanie na 0 1. z pieniedzmi nie mozna dzialac na float!!!

reszta = banknot - zakup

print(f"Do wydania {reszta} złotych")

#w monetach bedzie na listach - ile moent sie miesci w reszcie i wpisz do drugiej listy

for indeks, moneta in enumerate(monety):
    if reszta >= moneta:
        ilosc = reszta//moneta
        wartosc = ilosc*moneta
        reszta = reszta - wartosc

        wydac[indeks] = ilosc

print("W monetach")
for moneta, ilosc in zip(monety, wydac):
    print(moneta, '-', ilosc)