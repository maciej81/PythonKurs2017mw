# 2. obliczanie roku przestępnego
# podzielny przez 4, nie podzielny przez 100 ale podzielny przez 400

# znalezione w googlach: ((rok mod 4 = 0) and (rok mod 100 <> 0)) or (rok mod 400 = 0)
# Początkowo zgodnie z kalendarzem juliańskim wprowadzonym przez Juliusza Cezara w 45 roku p.n.e, rok przestępny występował co 4 lata
# Obecnie stosuje się formułę zgodną z kalendarzem Gregoriańskim wprowadzonym w 1582 roku przez papieża Grzegorza XIII
# dlatego zakladam, że rok należy podać jako 4 cyfry :)

rok = input("Podaj rok (format yyyy): ")

if rok.isnumeric() and len(rok)==4:
    print("Zaczynamy")
    #zamieniamy string rok na int rok do obliczen
    rok = int(rok)

    #sprawdzamy wg googla
    if (rok % 4 == 0 and rok % 100 !=0) or rok % 400 == 0:
        print(f"{rok} jest rokiem przestępnym")
    else:
        print(f"{rok} nie jest rokiem przestępnym")
else:
    print("Podaj same cyfry w formacie yyyy")

print("Koniec")