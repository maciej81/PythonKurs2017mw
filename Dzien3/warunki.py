# warunki if else elif

# if (warunek):
# elif (inny warunek):
# elif (jeszcze inny warunek):
# else:

if True:
    pass

#pass nic nie rob (po prostu sie zakonczy z exit code 0

print("--------")

x = 5
y = input("podaj liczbe calkowita:\n")

print(y)
print (type(y))
#wszystkie zmienne z input sa stingiem!!!!!

# jak chcesz miec int to musisz tak
# z = int(input("podaj jeszcze raz:\n"))

# print(z)
# print(type(z))

#isnumeric chyba sprawdza czy jest calowita, bo juz nie ogarnia float
if y.isnumeric():
    print("to jest liczba")
else:
    print("to nie jest liczba calowita")

if x < int(y):
    print(f"liczba {x} jest mniejsza od podanej {y}")
elif x == int(y):
    print(f"liczba {x} jest równa podanej {y}")
else:
    print(f"liczba {x} jest wieksza od podanej {y}")
