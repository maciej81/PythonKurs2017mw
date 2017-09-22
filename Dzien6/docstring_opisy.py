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