# napisac w petli mozliwosci userowi 1. dodanie imienia, 2. usuniecie imienia, sprawdzenie czy jest w bazie, sprawdzdenie ilosci imion

# wyswietla cala zawartosc listy
def lista_wyswietl(imiona):
    print("Wyswietlam całą listę")
    if imiona == None:
        print("Lista nie istnieje")
    else:
        if len(imiona) == 0:
            print("Lista jest pusta")
        else:
            print(imiona)

# dodaje imie do listy
def lista_dodaj(imie, imiona):
    print(f"Dodaję {imie} do listy")
    imiona.append(imie.capitalize())
    return imiona

#usuwa imie z listy, poniewaz dodaj dziala jako imie.capitalize() tu musze tak usuwac
def lista_usun(imie, imiona):
    imie = imie.capitalize()
    print(f"Usuwam {imie} z listy")
    if imie in imiona:
        imiona.remove(imie)
    else:
        print(f"{imie} nie istnieje na liście")

# sprawdza czy imie jest na liscie
def lista_sprawdz(imie, imiona):
    imie = imie.capitalize()
    if imie in imiona:
        print(f"{imie} jest na liście")
    else:
        print(f"{imie} nie istnieje na liście")

# zwraca dlugosc listy
def lista_dlugosc(imiona):
    return(len(imiona))

# wyswietla menu i czeka na input usera. zwraca wybrana wartosc
# jezeli user poda litere albo wartosc inna niz w menu to nie konwertuje do int. Takie przypadki powinny wpasc do warunku else w glownej petli
def wybor_menu():
    text_menu = "Co chcesz zrobić?\n" \
        "1. Wyświetl zawartość listy\n" \
        "2. Dodaj imię do listy\n" \
        "3. Usuń imię z listy\n" \
        "4. Sprawdź czy imię jest na liście\n" \
        "5. Sprawdź ilość imion na liście\n" \
        "0. Koniec\n"

    wybor = input(text_menu)
    if wybor.isnumeric():
        return int(wybor)
    else:
        return wybor

# glowna petla
# na razie bedzie tylko jedna lista imion, potem pomysle jak dodawać wiele list
lista_imion = []
user_input = wybor_menu()
while user_input:
    if user_input == 1:
        lista_wyswietl(lista_imion)
        user_input = wybor_menu()
    elif user_input == 2:
        imie = input("Podaj imię, które chcesz dodać: ")
        lista_dodaj(imie, lista_imion)
        user_input = wybor_menu()
    elif user_input == 3:
        imie = input("Podaj imię, które chcesz usunąć: ")
        lista_usun(imie, lista_imion)
        user_input = wybor_menu()
    elif user_input == 4:
        imie = input("Podaj imię, które szukasz: ")
        lista_sprawdz(imie, lista_imion)
        user_input = wybor_menu()
    elif user_input == 5:
        print(f"Lista zawiera {lista_dlugosc(lista_imion)} elementów")
        user_input = wybor_menu()
    else:
        print("Nieprawidłowy wybór. Jeszcze raz")
        user_input = wybor_menu()
print("Do widzenia")