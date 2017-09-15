#podaj haslo, haslo musi miec min 6 znakow, litery i cyfry


haslo = input("Wpisz haslo: ")

# while len(haslo) < 6 and haslo.isalnum(): to nie zadziala
#     print("haslo jest nieprawidłowe")
#     haslo = input("Wpisz haslo: ")
#
# print("Koniec")

prawidlowe = False

#tak bez sensu zagniezdzenie, bo kiedy bedzesz sie pytac o nowe?
while not prawidlowe:
    if len(haslo) < 6:
        print("Haslo za krotkie")
        haslo = input("Wpisz haslo: ")
    elif haslo.isalpha():
        print("Haslo musi zawierac cyfry")
        haslo = input("Wpisz haslo: ")
    elif haslo.isnumeric():
        print("Haslo musi zawierac litery")
        haslo = input("Wpisz haslo: ")
    else:
        print("Haslo dobre")
        prawidlowe = True

