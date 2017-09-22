# napisac w petli mozliwosci userowi 1. wyswietl do bazy 2. dodaj do bazy 3. usun z bazy itp
# czeka na usera akcje i cos robi

#chce czyscic output od czasu do czasu, uzyje do tego modulu os i 'cls'

import os

def clear():
    os.system('cls')

#definicje funkcjo do modyfikacji/wyswietlania zawartosci list
#na razie sam text - w celu sprawdzenia czy petla while dziala
def lista_wyswietl():
    print("Wyswietlam zawartość konkretnej listy")

def lista_dodaj():
    print("Dodaję zawartość do konkretnej listy")

def lista_usun():
    print("Usuwam zawartość z konkretnej listy")

def usun_liste():
    print("Usuwam całą listę")

#wyswietla menu i czeka na input usera. zwraca wybrana wartosc
def wybor_menu():
    #na razie tego nie daje pozniej bede czekac na user input czy wysc do glownego menu. i wtedy to odkomentuje
    #clear()
    text_menu = "Co chcesz zrobić?\n" \
                "1. Wyświetl istniejące listy\n" \
                "2. Dodaj elementy do listy\n" \
                "3. Usuń elementy z listy\n" \
                "4. Usuń całą listę\n" \
                "0. Koniec\n"

    wybor = input(text_menu)
    if wybor.isnumeric():
        return int(wybor)
    else:
        return wybor

# def wyjscie_menu():
#     wybor = input("Czy wyjść do menu głównego (T/N)?: ")

#glowna petla
user_input = wybor_menu()
while user_input:
    if user_input == 1:
        lista_wyswietl()
        user_input = wybor_menu()
    elif user_input == 2:
        lista_dodaj()
        user_input = wybor_menu()
    elif user_input == 3:
        lista_usun()
        user_input = wybor_menu()
    elif user_input == 4:
        usun_liste()
        user_input = wybor_menu()
    else:
        print("Nieprawidłowy wybór. Jeszcze raz")
        user_input = wybor_menu()
clear()
print("Do widzenia")