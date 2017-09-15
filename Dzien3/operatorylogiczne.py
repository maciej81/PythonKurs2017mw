#operatory logiczne

print(True)
print(False)
print(type(True))

#z wielkiej pisza sie slowa kluczowe, nie mozna nazw uzywac jako funkcji albo zmiennej

# == operator rownosci
# != operator nierownosci

print(True==True)
print(True!=False)

print("----------")

# and
# or

#obie strony musza byc prawdziwe aby cale bylo True
print (True and True)

#wystarczy jedna strona aby calosc byla prawdziwa
print (True or True)

print (True and False)
print (True or False)

# operator not zaprzeczenie
print(not True)

#kolejnosc operaotrow not and true
#w matematyce ** x/ +-

print("----------")
# operatory logiczne zawierania sie
# in, not in

s = "ciag znakow"

print("m" in s)
print("a" in s)
#resultatr Ture/False

print("----------")

# operator is
print (s is str)
#tu cos chodzi o to, ze porownujesz obiekt s do typu string i to nie dziala chyba
print(type(s))

