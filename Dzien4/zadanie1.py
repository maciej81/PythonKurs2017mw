#wydrukowac liczby od 0 do 100, jezeli liczba jest podzielna przez 3 to zamiast liczby drukuj fizz
#jezeli liczba jest podzielna przez 5 to drukuj Buzz
#jezeli podzielna przez 3 i 5 to drukuj FizzBuzz

for i in range(101):
    if i%15 == 0:
        print("FizzBuzz")
    elif i%3 ==0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
#to podobno mozna jeszcze skrocic, o jednego ifa?