# pliki tekstowe - znaki na ascii i mozna w edytorze otworzyc i przeczytac
# pliki binarne - jakos skompilowane itp, maja zadanie, nie da sie go otworzyc w notatniku bo krzaki beda, np skombilowany kod exe

# sa jeszcze pliki spakowane, takie jak docx. mozna je rozpakowac, w srodku sa xml

#sciezki do plikow trzeba uwazac bo np backslash bedzie wykonywac jakis kod typu \t \n
#trzeba albo \\ (ucieczka)
#albo r"c:\abc" - literka r przed stringiem. on wtedy to traktuje doslownie (stringa)

# print("c:\torba") #to nie zadziala prawidłowo
# print("c:\\torba") #tak jest ok
# print(r"c:\torba") #to tez jest ok, lepsze do pisania sciezek

# tryby otwierania plikow: r - read only, w - write will overwrite the whole file, a - amend/add to file, r+ = rw
# r jest domyslny

plik = open("dane")
print(type(plik))

linijka = plik.readline()

print(linijka, end='')

#readline czyta linie i ustawia kursor na nastepna
linia2 = plik.readline()

#do tego readline czyta razem z nowa linia na koncu
#print do tego dodaje nowa linie takze, default end = '\n' trzeba o tym pamietac
print(linia2, end='')

pozostaly_text = plik.read()

print(pozostaly_text)

#jezeli otwieramy plik to potem nalezy go zamknac. zawsze
plik.close()

#mozna readlines() - to stworzy liste z linijek tekstu
#open("dane", "r", encoding='utf8') - jezeli problem z kodowaniem np...
