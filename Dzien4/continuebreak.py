# a co jezeli nie dla wszystkich indeksow cos chcesz robic? np chcesz pominac jakis
#continue - olej petle i idz dalej w petli
#break - koniec petli

#taki przyklad - wydrukuj liczby z zakresu ale pomic podzielne przez 66

#continue pomija dalsze instrukcje i idzie w petli od nowa z nastepnym indeksem
for i in range(20, 100):
    if i%66 == 0:
        continue
        print("To sie nie wykona bo jest za continue")
    print(i)

#to samo bys mial tak
# for i in range(20,100):
#     if not i%66 == 0:
#         print(i)

#break wychodzi z petli
for i in range(20, 100):
    if i%66 == 0:
        break
    print(i)
