import sys
import os

#lista folderow w ktorej python szuka moduly ktore importujemy
#to jest PYTHON nie pycharm.
print("foldery robocze Python:", sys.path)


print("aktualny folder roboczy:", os.getcwd())

#pycharm ma inne sciezki - sam sobie podstawia. Python moze nie wiedziec o tych folderach
#to jest wazne przy imporcie modulow.
#mozna dodac python path do zmiennych srodowiskowych
#mozna wrzucac moduly do glowym bibliotek pythona, ktore powstaly przy instalacji
#mozna to w kodzie obsluzyc

#moduly pythona pypi - https://pypi.python.org/pypi
#mozna zainstalowac modul poprzez pip i potem go zaimportowac do kodu i uzywac
