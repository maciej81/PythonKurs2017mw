if __name__ == '__main__':
    with open('dane', 'w') as plik:
        print(plik.tell())

        s1 = "Ala ma kota"
        s2 = "jakis tekst znowu"
        s3 = "końcowy string"

        lista = [s1, s2, s3]

        plik.writelines(s+'\n' for s in lista)

        #write nie dodaje nowej lini. trzeba o to zadbac


