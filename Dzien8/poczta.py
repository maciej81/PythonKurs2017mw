# ten mailer nie obsluguje polskich liter
import smtplib
from Dzien8 import secrets

adresat = secrets.login
nadawca = secrets.login
haslo = secrets.haslo

# tworze silnik mailera
mailer = smtplib.SMTP("smtp.gmail.com", 587)
# witam się z serwerem / nawiązuję połączenie
mailer.ehlo()
#szyfruje polaczenie
mailer.starttls()
# teraz moge sie zalogowac
mailer.login(nadawca, haslo)

temat = "Subject: Temat wiadomosci\n"
wiadomosc ="To jest moja wiadomosc"
tresc = temat + wiadomosc

#wysylam
mailer.sendmail(nadawca, adresat, tresc)
print("Wysłano wiadomość")

mailer.close()

