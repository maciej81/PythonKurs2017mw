# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

#podaj dl. bokow
bok_a = input("Podaj dlugosc a: ")
bok_b = input("Podaj dlugosc b: ")
bok_c = input("Podaj dlugosc c: ")

if bok_a.isnumeric() and bok_b.isnumeric() and bok_c.isnumeric():
    print("Zaczynamy!")

    bok_a = int(bok_a)
    bok_b = int(bok_b)
    bok_c = int(bok_c)

    if (bok_a < bok_b + bok_c) and (bok_b < bok_a + bok_c) and (bok_c < bok_a + bok_b):
        print("Mozna narysowac trojkat")

        if (bok_a == bok_b) and (bok_a == bok_c):
            print("Jest to trójkąt równoboczny")
        elif (bok_a == bok_b) and (bok_a != bok_c):
            print("Jest to trojkąt równoramienny")
        else:
            print("Jest to trojkąt różnoboczny")

    else:
        print("Z tej mąki chleba nie będzie")

else:
    print("Podales nieprawidlowe dane")