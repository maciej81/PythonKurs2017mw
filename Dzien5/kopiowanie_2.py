nabial = ["mleko", "jajaka", "ser"]
chemia = ["domestos", "płyn do naczyń"]

#tutaj nie kopiuje wartosci, tworzy referencje do 2 list.
#to dlatego, ze lista jest obiektem, nie jest prostą zmienną. jak dodajesz obiekt to dodajesz referencje do niego/adres
#to jest typ 'referencyjny'

zakupy_wrzesien = [nabial, chemia]
print("wrzesień: ", zakupy_wrzesien)

zakupy_pazdziernik = zakupy_wrzesien.copy()
print("pazdziernik: ", zakupy_pazdziernik)

zakupy_listopad = [x for x in zakupy_wrzesien]
print("listopad: ", zakupy_listopad)

zakupy_wrzesien[1].append("gąbki")
print("wrzesień: ", zakupy_wrzesien)
print("pazdziernik: ", zakupy_pazdziernik)
print("listopad: ", zakupy_listopad)

#ciekawe jak on to rozpoznaje, ze lista zawiera proste czy zlozone i inaczej to traktuje...
#to pewnie interpreter robi
print(type(nabial))
print(type(zakupy_wrzesien))

