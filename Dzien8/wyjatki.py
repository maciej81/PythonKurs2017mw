# przechwytywanie wyjatkow (zamiast sprawdac czy plik istnieje to probujemy a jezeli sie nie uda to cos robimy)
# przechwytywanie jest pasywne - probuj cos robic a jak sie nie uda to cos z tym zrobimy
# aktywne jest najpierw sprawdzenie czy cos mozemy zrobic i dopiero robienie (czyli np. sprawdz czy plik istnieje)

# ponizej jest forma aktywna:
def moja_funkcja_aktywna():
    # modul os ma funkcje do terminala komend
    import os

    sciezka = 'plik2'

    if os.path.exists(sciezka):
        with open(sciezka) as plik:
            zawartosc = plik.read()
            print(zawartosc)
    else:
        print("Plik nie istnieje")

# a teraz to samo ale pasywnie czyli przechwytywanie wyjatkow

# try except finally
# except mozesz miec dowolna ilosc
# except moze rozne typy bledow miec
# finally sie wykona zawsze, jest opcjonalne

# typy bledow
# najbardziej ogolny - Exception
# ponizej ValueError
# NameError itp.
# bloki except najpierw definiujemy od najbardziej szczegółowych do najbardziej ogólnych
# w przypadku kilku błędów tylko jeden except sie wywoła
# to działa troche podobnie jak if elif else

try:
    with open("plik2") as plik:
        zawartosc = plik.read()
        print(zawartosc)

# wazna jest kolejnosc except. bo wykona sie tylko pierwszy, dlatego najpierwsz sie szczegolowe robi a na samym koncu ogolny Exception
except FileNotFoundError as e: #moge sobie przechwycic do obiektu/zmiennej i cos dalej z tym zrobic
    print("Plik nie istnieje", e)

except Exception:
    print("Pojawił się jakiś błąd")

finally:
    print("To się także wykona")