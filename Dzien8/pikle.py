# pozwala zapisywac obiekty całe
# zapisuje to binarnie do pliku
# zachowuje caly obiekt z uwzględnieniem typów itp
# pickle dziala binarnie dlatego odpowiedni tryb musisz wybrac

# jest jeszcze dill - zapisanie całej bieżącej sesji (wszystkich zmiennych, w kodzie obiektów itp)

import pickle

dane = [["TOmasz", "Kowąłśki", 36], ["Joanna", "Nowak", 28]]

#otwierasz plik w trybie binarnym
with open("plik.pkl", "wb") as plik:
    pickle.dump(dane, plik)

#dump zapisuje w systemowym/pycharm default kodowaniem. troche glupie. ale przy odkodowaniu moga byc problemy