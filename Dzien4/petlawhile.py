#while warunek True:
#   jakis kod
#   update warunku na Fales / inaczej petla nigdy sie nie skonczy
# while sie stosuje czesto jako 'czekajnik' na dane wejsciowe. User musi np wpisac dokadnie 6 cyfr jako haslo

stan = True

while stan:
    print("Hello")
    stan = False

print("-----------")

liczba = 1
while liczba <= 100:
    if liczba%2 == 0:
        print(f"{liczba} jest parzysta")
    else:
    print(f"{liczba} jest nieparzysta")
    liczba+=1

    # while w kolekcjach
    # chcemy przesc przez kolekcje (np string) i chcemy cos wybrac z tego stringa/stringu :)

imie = "Joanna"
indeks = 0

    while indeks < len(imie):
        print(imie[indeks], end=' ')
        indeks += 1
