import pickle

with open("plik.pkl", "rb") as plik:
    baza = pickle.load(plik)

print(type(baza))

print(baza)

#sprawdzenie zmiennych lokalnych i globalnych
print(locals())
print(globals())

