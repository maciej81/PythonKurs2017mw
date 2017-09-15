# ile jest liter, cyfr, malych liter, duzych liter w stringu
#uzywajac modulu string

import string

litery = 0
cyfry = 0
male_lit = 0
duze_lit = 0

zdanie = input("napisz coś: ")

for c in zdanie:
    if c.isdigit():
        cyfry+=1
    elif c.isalpha():
        litery+=1
        if c in string.ascii_lowercase:
            male_lit+=1
        else:
            duze_lit+=1

print(f"łącznie znaków jest {len(zdanie)} w tym: liter {litery}, małych {male_lit}, dużych {duze_lit},  cyfr {cyfry}")
#len daje dlugosc razem ze spacjami
#in string.ascii_lowercase - nie liczy spacji :) bo liczy aski