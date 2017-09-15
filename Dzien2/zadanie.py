#Napisać program, który zmieni string wejściowy „Ala ma kota, kot ma 4 nogi.”
# na string „Arek lubi psy, a najbardziej boksery!”
# Nie wolno dostarczać bezpośrednio literek!!! Można dowolnie przekształcać string wejściowy.

start_sting = "Ala ma kota, kot ma 4 nogi."
expected_string = "Arek lubi psy, a najbardziej boksery!"
start_sting_len = len(start_sting)
expected_sting_len = len(expected_string)
print(f"Długość teksu orginalnego {start_sting_len} oraz oczekiwanego {expected_sting_len}")

#create empty list, placeholder of ascii codes my start_string_ascii will already have expected length
#to compare ascii codes later on and change them if they are not equal
start_sting_asci = [0]*(expected_sting_len)
expected_sting_asci = [0]*(expected_sting_len)

#save ascii for my stings, using two loops as my start_sting has different length
for i in range (0, start_sting_len):
    start_sting_asci[i] = ord(start_sting[i])

for i in range (0, expected_sting_len):
    expected_sting_asci[i] = ord(expected_string[i])

print(start_sting_asci)
print(expected_sting_asci)

#go through the list of codes, compare them and change start_sting_asci if codes are different
for i in range (0, expected_sting_len):
    if start_sting_asci[i]!=expected_sting_asci[i]:
        start_sting_asci[i]=expected_sting_asci[i]

final_string_array = [None]* (expected_sting_len)

for i in range (0, expected_sting_len):
    final_string_array[i] = chr(start_sting_asci[i])

final_string = "".join(final_string_array)
print(final_string)