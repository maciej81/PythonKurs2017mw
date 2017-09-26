with open('dane', 'a') as plik:
    plik.write('dopisana linijka ąę')

    #w trybie a otiwera kursor na ostatniej pozycji

    #nie bylo znaku nowej lini wiec dopisal

    #jak dopisac ale zeby najpierw sprawdzil czy jest nowa linia czy nie
    #i jezeli nie to ma dodac i wpisac

    # jak zapisujemy pliki dobrze jest zapisywac z nowa linia z automatu
    plik.write('moja nowa linijka\n')

    # plik.seek(-1)  #seek nie zadziala bo plik w trybie a jest nie do odczytu
    #tylko i wylacznie do zapisu. nie mozna przemieszczac kursora i czytac :)


    # znak = plik.read(1)
    #
    # if znak == '\n':
    #     plik.write('moja nowa linijka w nowej linii')
    # else:
    #     plik.write()

    #jak zapisujemy pliki dobrze jest zapisywac z nowa linia z automatu

    #tryb w to nadpisze wszystko! dane usuniete.