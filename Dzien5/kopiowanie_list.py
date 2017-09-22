#kopiowanie list z typami prostymi (niezmienne: int, string itp)

wynik = 3

lista_a = ["zero", "jeden", wynik]

print("lista a: ", lista_a)

wynik = 43
#zmienilem wynik, ale moja lista sie nie zmienia. ona trzyma wartosc wynik, a nie referencje do niej.

print("lista a: ", lista_a)

#copy tez kopiuje wartosci
lista_b = lista_a.copy()
print("lista b: ",lista_b)

#nawet jak cos dodam do a to b sie nie aktualizuje
lista_a.append("Nowy")

print(lista_a)
print(lista_b)

#bo one sa w innej pamieci
print(hex(id(lista_a)))
print(hex(id(lista_b)))