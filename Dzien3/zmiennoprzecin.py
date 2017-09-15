x = 0.3

print (f"{x:f}")

print (f"{x:.2f}")

print("{0:.2F}".format(x))
#wydrukuj od 0 do .2f (2 miejsca po przecinku float)
#nie kumam zapisu, mozna .2f albo 2f jaka jest roznica?
#.2f dwa miejsca po przecinku jako float
# F 6 miejsc po przecinku bo to standard

a = 0.3
b = 0.1 + 0.1 + 0.1

print (a)
print (b)

print (type(a))
print (type (b))
#bo nie wszystkie liczby dziesietne mozna dokladnie przedstawic w systemie binarnym
#0.1 sie nie da przedstawic dokladnie bo to jest 1/10
# a dwojkowo masz nastepujace liczny 1/2 1/4 1/8 1/16 (czyli ujemne potegi 2)
# i dlatego 0.1 masz tylko w przyblizeniu binarnie

#liczby dziesietne mozna inaczej przedstawiac np typ decimal,
# to jest problem jezeli pracujesz z liczbami, finansami itp
