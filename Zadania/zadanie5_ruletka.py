# 5. ruletka: otrzymawszy liczbę, sprawdź czy jest ona:
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta

# tabelka z liczbami koloru czerwonego
red_colour_table = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]

liczba = input("Podaj liczbę od 0 do 36: ")

if liczba.isnumeric():
    liczba = int(liczba)

    #sprawdz zakres liczb
    if (liczba <=36) and (liczba >=0):
        print(f"Obstawiłeś liczbę {liczba}")

        #sprawdz czy parzysta/nieparzysta
        if liczba % 2 == 0:
            print("Jest to liczba parzysta")
        else:
            print("Jest to liczba nieparzysta")

        #sprawdz małe czy duże numery
        if liczba <= 18:
            print("Obstawiłeś małe numery")
        else:
            print("Obstawiłeś duże numery")

        #sprawdz kolor
        if liczba in red_colour_table:
            print("Obstawiłeś kolor czerwony")
        elif liczba == 0:
            print("Obstawiłeś kolor zielony")
        else:
            print("Obstawiłeś kolor czarny")
    else:
        print("Podałeś liczbę spoza zakresu ruletki")

else:
    print("Podałeś nieprawidłowe dane. Podaj liczbę od 0 do 36")