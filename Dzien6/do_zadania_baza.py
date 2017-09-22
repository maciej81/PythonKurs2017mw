def dodaj_imie(imie, imiona=[]):
    imiona.append(imie.capitalize())
    return imiona

# baza = ["Ala"]
# dodaj_imie("Tomasz", baza)
# print(baza)

#co jak podam bez listy? zostanie stworzona jakas lista domyslna i zwrocimy ja

nowa_baza = dodaj_imie("Marek")
print(nowa_baza)

nowa_baza = dodaj_imie("Agnieszka")
print(nowa_baza)

jeszcze_inna = dodaj_imie("Enda")

print(jeszcze_inna)

#w taki sposob nie tworzy nowych list, przy kolejmym wywolaniu bedzie wskazywac te sama liste.
# czemu?
# po python argumenty domyslne dla danej funkcji waliduje tylko raz! potem juz olewa
# skoro argumentem domyslnym jest typ zlozony (lista) to potem python ja pamieta

#jak to obejsc?
# domyslnie argument podac jako None i w funkcji jezeli argument nie jest none to tworz nowe
# to dotyczy wszystkich typow zlozonych, nie powinno sie ich uzywac jako domyslne - tylko inicjuj z None a potem w funkcj definiuj
# w sensie jezeli twoja funkcja ma tworzyc nowe zmienne zlozone (albo przyjmowac istniejace jako argument)...
def dodaj_imie2(imie, imiona=None):
    if imiona == None:
        imiona = []
    imiona.append(imie.capitalize())
    return imiona

nowa_baza2 = dodaj_imie2("Marek")
print(nowa_baza2)

nowa_baza2 = dodaj_imie2("Agnieszka")
print(nowa_baza2)

dodaj_imie("Krzys", nowa_baza2)
print(nowa_baza2)

jeszcze_inna2 = dodaj_imie2("Enda")

print(jeszcze_inna2)

