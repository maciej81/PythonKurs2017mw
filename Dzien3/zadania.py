#sprawdz czy liczba jest podzielna przez 3 i 5 i 7

liczba = input("podaj liczbe: ")

#sprawdz czy to jest liczba
if liczba.isnumeric():
    l = int(liczba)
    if l%3 == 0:
        print("liczba jest podzielna przez 3")
        if l%5==0:
            print("liczba jest podzielna przez 3 i 5")
            if l%7:
                print ("liczba jest podzielna przez 3 i 5 i 7")
else:
    print("podaj tylko liczbe")


#to samo inaczej przy uzyciu operatora and to jest lepsze

# sprawdz czy to jest liczba
if liczba.isnumeric():
    l = int(liczba)
    if l % 3 == 0 and l%5 == 0 and l%7:
        print("liczba jest podzielna przez 3 i 5 i 7")
    else:
        print("liczba nie jest podzielna przez 3, 5 i 7")
else:
    print("podaj tylko liczbe")