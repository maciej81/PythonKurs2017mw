#tryb r+ aka rw jest lepszy, mozna sie poruszac, pisac czytac itp

if __name__ == '__main__':
    with open('dane', 'r+') as plik:
        #rw otwiera plik na poczatku
        print(plik.tell())

        #zeby przejsc na sam koniec od razu mozna plik read
        plik.read()
        print(plik.tell())

        #ustawiam ostania pozycje do zmiennej i ustawiam sie wczesjniej o jeden
        pozycja = plik.tell()
        plik.seek(pozycja-1)

        #zczyta ostatni znak i ustawi sie za nim
        znak = plik.read(1)

        #jezeli ten znak to byla nowa linia to dodaj
        if znak == '\n':
            plik.write('moja nowa linia ąę\n')
        # a jezeli nie to najpierw dodaj nowa linie
        else:
            plik.write('\nmoja nowa linia ąę\n')