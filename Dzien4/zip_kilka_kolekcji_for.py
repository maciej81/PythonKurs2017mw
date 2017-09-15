kolekcja_a = "0123456789123456"
kolekcja_b = "Ala ma kota"

for el_a, el_b in zip(kolekcja_a, kolekcja_b):
    print (el_a, el_b)

#zip w petli for zadziala na najkrotszej kolekcji/zbiorze

#to samo inaczej, tylko, ze jezeli kolekcje beda roznej dlugosci to moze sie wywalic
# indeks = 0
# for el_a in kolekcja_a:
#     print(el_a, kolekcja_b[indeks])
#     indeks+=1

#jaki indeks ma dana wartosc z kolekcji
#enumerate - zwraca najpierw index a potem wartosc zakresu

wyraz = 'Joanna'

for index, litera in enumerate(wyraz):
    print(index, litera)





