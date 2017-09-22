# 1. sprawdź czy jest wygrana w kółko i krzyżyk

dostepne_znaki = ['x', 'o', 'n']
dane_wejsciowe = []

#w petli wezme dane od uzytkownika i utworze 2D macierz wynikow
i = 0

while i <= 2:
    dane_wejsciowe.append(list(input(f"Podaj {i+1} wiersz wyniku gry. Użyj 'n' jako pole puste: ")))
    i+=1

for i in dane_wejsciowe:
    print(i)

for i in range(3):
    for j in range(3):
        if dane_wejsciowe[i][j] in dostepne_znaki:
            print("Zaczynamy")
        else:
            print("Podałeś błędne dane")
            break

dane_wejsciowe.c