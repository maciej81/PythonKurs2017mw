 # drujuj kwadraty

#drukuj kwadraty z zakresu
def drukuj_kwadraty(x, y):
    for i in range(x, y + 1):
        print(i**2)

drukuj_kwadraty(2,4)

# python jest slabo-typowalny. Do momentu uzycia zmiennej ciezko jest powiedziec co i jak
# dlatego sie nie wpisuje jakiego typu argumenty funkcja przyjmuje
# mozna uzywac type - hintow

# pole trojkata 1/2ah
def pole_trojkata(a, h):
    pole = 0.5 * a * h
    print(pole)

pole_trojkata(4, 10)

#zmienne definiowane w funkcji sa widoczne tylko w funkcji. potem juz nie
# print(pole) #to sie wywali bo pole nie istnieje poza blokiem pole_trojkata

#mozna definiowac argumenty domyslne, przy wywolaniu mozna je pominac ale jak sie poda to je uzyje
# argumenty wymagane musza byc na poczatku, potem dopiero podaje sie domyslne z wartosciami

def drukuj_domyslnie_10_razy(y = 10):
    for i in range(y):
        print("text")

drukuj_domyslnie_10_razy()
print("---------")
drukuj_domyslnie_10_razy(3)