h = input("Podaj wysokość piramidy: ")

if h.isdigit():
    h = int(h)
    hash = 1
    space = h-1
    for i in range(h):
        print(" "*space, end="")
        print("#"*hash)
        hash+=2
        space-=1
else:
    print("Można podawać tylko liczby całkowite")
