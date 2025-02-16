import httpx
from datetime import date

print("Online prevodnik men dle cnb")

today = date.today().strftime("%d.%m.%Y")

url = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date={today}'
r = httpx.get(url)

lines = r.text.split("\n")

row = ''
def hledani_kurzu(mena):
    for line in lines:
        if f"|{mena}|" in line:
            row = line
    if row: 
        return row
    else: 
        print("Chyba při hledání měny")
        return None

def ziskej_kurz(line):
    line_arr = line.split("|")
    if line:
        line_str = line_arr[-1]
        line_str = line_str.replace(",", ".")
        kurz = float(line_str)
        return kurz

def z_czk_do_eur(castka, kurz_eur):
    return castka / kurz_eur

def z_eur_do_czk(castka, kurz_eur):
    return castka * kurz_eur

def z_czk_do_usd(castka, kurz_usd):
    return castka / kurz_usd

def z_usd_do_czk(castka, kurz_usd):
    return castka * kurz_usd

def z_usd_do_eur(castka, kurz_eur, kurz_usd):
    return (castka / kurz_usd) * kurz_eur

def z_eur_do_usd(castka, kurz_usd, kurz_eur):
    return (castka / kurz_eur) * kurz_usd

line_eur = hledani_kurzu("EUR")
line_usd = hledani_kurzu("USD")

kurz_eur = ziskej_kurz(line_eur)
kurz_usd = ziskej_kurz(line_usd)

print(f"EUR {kurz_eur}")
print(f"USD {kurz_usd}")

prevody = [
    "z CZK do EUR",
    "z EUR do CZK",
    "z CZK do USD",
    "z USD do CZK",
    "z USD do EUR",
    "z EUR do USD",
]
print("Dostupne prevody:")
for i, prevod in enumerate(prevody, start=1):
    print(f"{i}. {prevod}")


exchange_type = input("Zadej cislo prevodu: ")

if not exchange_type.isdigit():
    print("Chybne zadane cislo prevodu")
    exchange_type = input("Zadej cislo prevodu: ")

exchange_type = int(exchange_type)

if exchange_type < 1 or exchange_type > 6:
    print("Chybne zadane cislo prevodu")
    exchange_type = input("Zadej cislo prevodu od 1 do 6: ")

result = None

if exchange_type == 1:
    vstup = input("Zadej castku v CZK: ")
    castka = vstup

    if not vstup.isdigit():
        print("Chybne zadana castka")
        vstup = input("Zadej castku v CZK: ")
        castka = int(vstup)
        result = z_czk_do_eur(castka, kurz_eur)
    else:
        castka = int(vstup)
        result = z_czk_do_eur(castka, kurz_eur)
elif exchange_type == 2:
    vstup = input("Zadej castku v EUR: ")
    castka = vstup

    if not vstup.isdigit():
        print("Chybne zadana castka")
        vstup = input("Zadej castku v EUR: ")
        castka = int(vstup)
        result = z_eur_do_czk(castka, kurz_eur)
    else:
        castka = int(vstup)
        result = z_eur_do_czk(castka, kurz_eur)
elif exchange_type == 3:
    vstup = input("Zadej castku v CZK: ")
    castka = vstup

    if not vstup.isdigit():
        print("Chybne zadana castka")
        vstup = input("Zadej castku v CZK: ")
        castka = int(vstup)
        result = z_czk_do_usd(castka, kurz_usd)
    else:
        castka = int(vstup)
        result = z_czk_do_usd(castka, kurz_usd)
elif exchange_type == 4:
    vstup = input("Zadej castku v USD: ")
    castka = vstup

    if not vstup.isdigit():
        print("Chybne zadana castka")
        vstup = input("Zadej castku v USD: ")
        castka = int(vstup)
        result = z_usd_do_czk(castka, kurz_usd)
    else:
        castka = int(vstup)
        result = z_usd_do_czk(castka, kurz_usd)
elif exchange_type == 5:
    vstup = input("Zadej castku v USD: ")
    castka = vstup

    if not vstup.isdigit():
        print("Chybne zadana castka")
        vstup = input("Zadej castku v USD: ")
        castka = int(vstup)
        result = z_usd_do_eur(castka, kurz_eur, kurz_usd)
    else:
        castka = int(vstup)
        result = z_usd_do_eur(castka, kurz_eur, kurz_usd)
elif exchange_type == 6:
    vstup = input("Zadej castku v EUR: ")
    castka = vstup

    if not vstup.isdigit():
        print("Chybne zadana castka")
        vstup = input("Zadej castku v EUR: ")
        castka = int(vstup)
        result = z_eur_do_usd(castka, kurz_usd, kurz_eur)
    else:
        castka = int(vstup)
        result = z_eur_do_usd(castka, kurz_usd, kurz_eur)

print(f"Vysledek je {result:.3f}")