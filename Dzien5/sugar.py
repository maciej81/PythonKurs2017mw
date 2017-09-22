#chce miec kwadraty liczb z listy
lista = list(range(1,10))
lista2 = []

print(lista)

for i in lista:
    lista2.append((i**2))

print(lista2)

#to samo inaczej uzywajac pythonowego jezyka :)
#tzw list comprehension
lista3 = [x**2 for x in lista]
print(lista3)

lista4 = [x**2 for x in lista if x % 3 == 0]
print(lista4)

lista5 = [x**2 for x in range(10)]
print(lista5)