#kolejka FIFO - first in first out

kolejka = []

kolejka.append(1)
kolejka.append(56)
kolejka.append(23)

print(kolejka)

#pop usuwa i zwraca element, ktory usuwa. normalnie pop usuwa od konca (czyli LIFO) ale jak sie poda index to nie
element = kolejka.pop(0)

print(element)
print(kolejka)

#kolejka LIFO - last in first out
print("-------------------")
stos = []
stos.append(87)
stos.append(108)
stos.append(33)
print(stos)

element2 = stos.pop()

print(element2)
print(stos)