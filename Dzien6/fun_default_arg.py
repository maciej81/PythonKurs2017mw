def wypisz_dane(imie, nazwisko, kurs = "Python", il_dni = 15):
    print(imie, nazwisko, kurs, il_dni)

wypisz_dane("Tomek", "Kowalski", "Java")

#kolejnosc jest wazna, nie mozna pominac niczego... to troche dlatego, ze nie wiesz jakie sa typy...
# jak pominac jakis argument?
wypisz_dane("Ktos", "Ktos", 17)

# uzywajac nazwy zmiennej, wtede nie trzeba podawac 3 zmiennej
# w taki sposob moza zmieniac kolejnosc podawania argumentow, ale musisz znac ich nazwy
wypisz_dane("Marek", "P", il_dni=40)

# argumenty wymagane, inaczej pozycyjne (w errorach bedzie cos takiego podane)
# pozycyjne bo sa pierwsze? na okreslonych pozycjach?

