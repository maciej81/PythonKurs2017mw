h = int(input("Podaj wysokość piramidy: "))
hash = 1
space = h-1

for i in range(h):
    print(" "*space, end="")
    print("#"*hash)
    hash+=2
    space-=1
