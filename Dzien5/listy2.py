#utworzyc liste wyrazow ze slowa, bez spacji
zdanie = "Ala ma kota i ma cztery lapy"
wyrazy = []
wyraz = ""

for i in zdanie:
    if i == " ":
        wyrazy.append((wyraz))
        wyraz = ""
    else:
        wyraz+=i
wyrazy.append(wyraz)

print(wyrazy)

#to samo inaczej

wyrazy2 = zdanie.split()
print(wyrazy2)


