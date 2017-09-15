#policzyc ile jest liczb parzystych i nieparzystych w range
zakres = range(11)
il_p = 0
il_np = 0

for i in zakres:
    if i%2 == 0:
        il_p+=1
    else:
        il_np+=1

print(f"Ilosc parzystych to {il_p} a nieparzystych {il_np}")
