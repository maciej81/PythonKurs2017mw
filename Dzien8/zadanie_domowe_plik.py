import os

sciezka_pliku = '/home/maciej/Documents/iSAPython3/day8/treasure_inside'

#poczatek i koniec dla jpg
# BMP : 42 4D
# JPG : FF D8 FF EO
# PNG : 89 50 4E 47
# GIF : 47 49 46 38

JPG_START = bytes(0xFFD8)

with open(sciezka_pliku, "rb") as plik:
    print("udało się otworzyć plik")

    bajt = plik.read(2)
    print(bajt)
    bajt = plik.read(2)
    print(bajt)
    bajt = plik.read(2)
    print(bajt)
    bajt = plik.read(2)
    print(bajt)
    print(type(bajt))

    for i in range(os.path.getsize(sciezka_pliku)):
        if plik.read(i) == JPG_START:
            print("cos znalazlem")

    print("nic nie znalazlem")

