#zeby nie pamietac o zamykaniu pliku mozna napisac tak
# to zadziala jak open i w tym przypadku nie musimy plik.close, jak sie skonczy blok to sie plik zamknie

with open("dane") as plik:

    #pokazuje na ktorej pozycji jest kursor
    print(plik.tell())
    linijka = plik.readline()

    #podaje gdzie sie znajduje kursor, tu moze byc inaczej na unix i windows bo maja clrf albo cl samo (liczy tez nowa linie)
    # do tego liczy sie indeks od 0 - pamietaj :)
    print(plik.tell())

    #read czyta znaki z pozycji
    znak = plik.read(1)

    print(znak)
    print(plik.tell())

    #idz na pozycje 2
    plik.seek(2)
    print(plik.read(1))
    print(plik.tell())