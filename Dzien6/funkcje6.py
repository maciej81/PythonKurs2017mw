imie = "jola"

def drukuj_imie(imie_2):
    global imie #to przestanie byc lokalna zmienna, imie bedzie juz sie odnosic do globalnej zmiennej

    nonlocal imie #tylko jeden poziom wyzej, nie globalnie ale tylko 1 wyzej

    imie = "ania".capitalize()
    imie_2 = imie_2.capitalize()

    print(imie, imie_2)

drukuj_imie("gosia")

#raczej sie z tego nie korzysta
# chyba ze z jakichs STAłYCH

