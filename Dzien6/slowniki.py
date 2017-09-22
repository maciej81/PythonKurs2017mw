#listy - kolejnosc jest wazna, jest indeksowana
#slowniki - kolejnosc nie jest wazna, nie ma indeksow
# - ma klucz - identyfikator, klucz musi byc typem niezmiennym
# wartosc moze byc dowolnym typem
# klucz musi byc unikalny
#odwojuemy sie przez klucz (nie indeks)!

# słownik {klucz:wartosc,}
# tuple (,)
# lista [,]

osoby = {"Ania":"Kowalska", 2:234.4, "9238732":4}
print(osoby[2])

#jezeli taki klucz juz istnieje to zostanie nadpisany
osoby["Joanna"] = "costam"

print(osoby)

print(osoby.keys())
print(osoby.items())
print(osoby.values())

#.items uzywamy w petlach glownie
#.items tworzy tupla
for key, value in osoby.items():
    print(key, value)

# jezei znasz kolejnsoc elementow i sa posortoane to raczej listy
# slowniki poniewaz nie jest wazna kolejnosc, ale sa bardzo szybkie bo po prostu bierzesz klucz
# hashowanie (jakis wstepny podzial problemu i zapis pod klucz. potem wystarczy 1. jaki klucz 2. potem tylko w tym kluczu szukamy dalej
# czyli jakis podzial problemu, do tego tez sie uzywa slownikow

# set - zbior / od razu jest posortowany
# mozna je dodawac (polaczyc), pomnozyc (koniunkcja) - matematyczne dzialania na zbiorach

