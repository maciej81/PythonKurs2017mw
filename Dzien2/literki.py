slowo = "jakis text"
dlugosc = len(slowo)


print("Słowo '{}' ma {} liter".format(slowo,dlugosc))

#od python 3.6 mozna zamiast .format uzywac f przed stingiem w taki sposob
print(f"Słowo '{slowo}' ma {dlugosc} liter")

#indexowanie
print(slowo[0])
print(slowo[-3])
#to samo inaczej
print(slowo[len(slowo)-3])

#'slajsowanie' :) dziala tak <, ) czyli prawy jest niedomkniety (nie uwzgledniamy go
print(slowo[2:5])
#w slajsowaniu drugi przedzial nie ma znaczenia? mozesz podaj poza indeksem np 100 i sie nie wywali
print(slowo[2:100])

#mozna krok co ktory wybrac, czyli od 1 do 7 co drugi
print(slowo[2:8:2])

#mozna w tyl indeksowac (przestawia od tylu)
print(slowo[::-1])

#mozna tez nie zamykac przedzialu
print(slowo[:5])
print(slowo[5:])

#ord zwraca kod z unicode znaku/ od A - Z maja taki sam jak ASCII
kod = ord("D")
print(kod)

#chr zmienia na znak
print (chr(kod+4))
