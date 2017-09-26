baza = []

with open('osoby.csv', 'r+') as plik:

    # lista kolumn - opis
    opis = plik.readline()

    # stip funkcja usuwa biale znaki z poczatku i konca
    print(opis.strip())

    #taka petla for zrobi readline
    for line in plik:
        # usuwamy whitespace
        line = line.strip()

        #lista elementow w line
        osoba = line.split(",")
        print(osoba)
        baza.append(osoba)

    baza.append(['Maciej', 'Kowalski4', '33'])

    print(baza)

    #teraz chce to zapisac do pliku spowrotem
    dane_zapis = []

    for osoba in baza:
        dane_zapis.append(",".join(osoba))

    print(dane_zapis)

    plik.seek(0)
    plik.writelines(dane_zapis)

# generalnie taka praca jest problematyczna. trzeba o wszystkim pamietac
# do tego np jak bedziesz miec stringi i do tego int to sie bedzie wywalac
# do csv jest modul csv :)