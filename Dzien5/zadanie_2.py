#zamien zdanie na liste wyrazow, bez przecinka

zdanie = "Ala ma kota, kot ma ale"

lista = zdanie.split()

# lista.remove(',') tak sie nie da, bo przecinek jest dolaczony do 'kota' jako obiekt. obiekt to 'kota,'
#czyli najpierw trzeba ze stringa usunac przecinek

zdanie = zdanie.replace(",", "")

lista2 = zdanie.split()

print(lista)
print(lista2)