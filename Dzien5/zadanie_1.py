#usun duplikaty z listy

lista = [10, 20, 30, 40, 20, 45, 20, 10, 49, 90, 35, 40]
lista_koncowa = []

for i in lista:
    if i not in lista_koncowa:
        lista_koncowa.append(i)

print(lista)
print(lista_koncowa)