print("Dzien dobry!")

# zmienna typu string
imie = "Ala"
print(imie)
print(3 * imie)

nazwisko = "kowalska"

print(imie + ' ' + nazwisko.capitalize())

#inne drukowanie strigow z uzyciem .format
print("{} {}".format(imie, nazwisko.capitalize()))

print("{1} {0} ma kota".format(imie, nazwisko.capitalize()))
