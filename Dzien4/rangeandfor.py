# range(stop)
# range(3) - <0,1,2> // len()==3
# albo iaczej piszac <0,1,2,3)

#range(start,stop)
#range(4,8) - <4,5,6,7>

#range(start, stop, krok)
#range(0,10,3) - <0,3,6,9>

#range zwraca inta
#range sie nie generuje caly od razu. po przejsciu kroku petli dopiero

zakres = range(4)

print(zakres)

#for element in zbiór/zakres:
#       kod

#for wykona kod tyle razy ile elementow znajduje sie w zbiorze/zakresie

for i in zakres:
    print(i)
    i+=1
    print("nowe i ", i)


wyraz = 'dlugiwyrajjakisbardzo'

for c in wyraz[::-1]:
    print(c)

