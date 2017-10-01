# mozna samemu wyzwolic wyjatek / specjalnie podniesc blad
# raise
# jezeli piszemy moduly, ktore beda przez kogos wykorzystywane
# i wiemy, ze np jakies dane sa nieprawidlowe
# przy duzych programach gdzie jest integracja wielo-zespolowa
# przekazujemy bląd i dalej ktoś to musi sobie sam obsłużyć

try:
    with open("dane.txt") as plik:
        print(plik.read())
except FileNotFoundError as e:
    print(e)
    print("Podany plik nie istnieje")

    raise ValueError("Błędna nazwa pliku")

except Exception:
    print("Nieoczekiwany błąd")

print("CDN")

# jak sie robi raise wyjatku to tak jakby break sie uruchomil