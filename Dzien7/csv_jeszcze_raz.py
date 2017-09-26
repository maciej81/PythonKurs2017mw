import csv

with open('osoby.csv') as plik:
    # tworzymy czytnik to zczyta plik i utworzy od razu liste
    czytnik_csv = csv.reader(plik)

    for line in czytnik_csv:
        print(line)


#zapis tez jest prosty, do tego obsluguje inty i str w jednym
dane = ['Adam', 'Kowalski5', 66]

with open('osoby.csv', 'a') as plik:
    #tworzy zapisywacz
    zapisywacz_csv = csv.writer(plik)
    zapisywacz_csv.writerow(dane)

