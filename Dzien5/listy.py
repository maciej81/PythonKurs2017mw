lista = [1,2,3]
print(type(lista[0]))
print(lista)

#listy zagniezdzone nie musza byc rowne
lista2 = [[1,2,3], [4,5,6], [7,8,9,10]]
print(lista2[2][3])
#i moga zawierac rozne typy
lista3 = [1, "jakis tekst", 2]
print(lista3[1])

#konstruktor
lista3 = list(range(2,6))

lista4 = list("kwiatek")
print(lista4)

#jak z listy zrobic stinga

flower = ""

for i in lista4:
    flower += i.upper()

print(flower)

#to samo inaczej. Najpier podajesz znak jakim chcesz polaczyc elementy z listy. potem join
flower2 = "".join(lista4)
print(flower2)

flower3 = "*".join(lista4)
print(flower3)

#czy da sie tak polaczyc liste intow? NIE DA SIE :) ponizsze nie zadziala
# lista_int = list(range(5))
# a = "".join(lista_int)
# print(type(a))

# do listy mozna dodawac/insert dane
lista5 = list(range(10))

lista5.insert(4,"ALa")
print(lista5)

#z listy mozna tez usuwac
del lista5[4]
print(lista5)
