#sprawdzic czy str jest palindromem
#pod definicja funkji klikasz ''' (albo """) i klikasz enter
#tam mozesz wtedy pisac
# argument hint:str -> to jest tylko wskazowka, mozna tak naprawde cokolwiek wpisac
# odwracanie stringu napisane jest w funkcje4 wiec moge sobie zaimportowac
# import jest z poziomu projektu, a moja funkcja jest w Dzien6.

from  Dzien6.funkcje4 import odwroc_str

def czy_palindrom(fraza:str):
    '''
    Sprawdza czy podana fraza jest palindromem (litery te same czytane od przodu i od tylu
    :param fraza: zdanie do sprawdzenie
    :return: True jeśli fraza jest palindromem
    '''

    for litera, litera2 in zip(fraza, odwroc_str(fraza)):
        if litera != litera2:
            return False    #return przerywa funkcje (dziala jak break). wiec nie musisz sie martwic, ze
        return True

print(czy_palindrom("kajak"))

#problem jest taki ze wykona wszystko z zaimportowanego modulu. nawet jezeli robisz import tylko jednej funckji
#dlatego w importowanych modulach nie powinno byc zadnych operacji bo sie wykona
#co zrobic aby tego uniknac - main :) czyli glowny program. to sie nie bedzie importowac, jezeli modul bedzie wykonywany
#bezposrednio a nie jezeli bedzie importowany piszesz main i tabulacja
#zmienna _name_ istnieje dla kazdego modulu.
#do tego sie jeszcze pakuje kod do funckcji main() i pod tym ifem tylko main() sie wykonuje
#do tego pliku, jak go uruchomisz w terminaly to sie python wywali. bo to pycharm sobie ustawil sciezki przy import
# a sam python nie wie o tym. pycharm podstawia swoje foldery. Dla python trzeba ustawiac sciezki recznie...
#mozna podac python path zmienna srodowiskowa w systemie
#mozna dodac liste w kodzie