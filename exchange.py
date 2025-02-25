import httpx
from datetime import date
import colorama
from colorama import Fore, Back, Style
from colorama import init

init()

print(Style.BRIGHT + Back.CYAN + Fore.BLUE + "Online prevodnik men dle cnb" + Style.RESET_ALL)

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
        print(Style.BRIGHT + Fore.RED + "Chyba při hledání měny" + Style.RESET_ALL)
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

print(Back.GREEN + Style.BRIGHT + f"EUR {kurz_eur}" + Style.RESET_ALL)
print(Back.GREEN + Style.BRIGHT + f"USD {kurz_usd}" + Style.RESET_ALL)

prevody = [
    "z CZK do EUR",
    "z EUR do CZK",
    "z CZK do USD",
    "z USD do CZK",
    "z USD do EUR",
    "z EUR do USD",
]
print(Style.BRIGHT + Fore.BLUE + "Dostupne prevody:" + Style.RESET_ALL)
for i, prevod in enumerate(prevody, start=1):
    print(Fore.MAGENTA + f"{i}. {prevod}" + Style.RESET_ALL)


exchange_type = input(Fore.YELLOW + "Zadej cislo prevodu: " + Style.RESET_ALL)

if not exchange_type.isdigit():
    print(Style.BRIGHT + Fore.RED + "Chybne zadane cislo prevodu" + Style.RESET_ALL)
    exchange_type = input(Fore.YELLOW + "Zadej cislo prevodu: " + Style.RESET_ALL)

exchange_type = int(exchange_type)

if exchange_type < 1 or exchange_type > 6:
    print(Style.BRIGHT + Fore.RED + "Chybne zadane cislo prevodu" + Style.RESET_ALL)
    exchange_type = input(Fore.MAGENTA + "Zadej cislo prevodu od 1 do 6: " + Style.RESET_ALL)

result = None

if exchange_type == 1:
    vstup = input(Style.BRIGHT + Fore.CYAN + "Zadej castku v CZK: " + Style.RESET_ALL)
    castka = vstup

    if not vstup.isdigit():
        print(Style.BRIGHT + Fore.RED + "Chybne zadana castka" + Style.RESET_ALL)
        vstup = input(Style.BRIGHT + Fore.CYAN + "Zadej castku v CZK: " + Style.RESET_ALL)
        castka = int(vstup)
        result = z_czk_do_eur(castka, kurz_eur)
    else:
        castka = int(vstup)
        result = z_czk_do_eur(castka, kurz_eur)
elif exchange_type == 2:
    vstup = input(Style.BRIGHT + Fore.CYAN + "Zadej castku v EUR: " + Style.RESET_ALL)
    castka = vstup

    if not vstup.isdigit():
        print(Style.BRIGHT + Fore.RED + "Chybne zadana castka" + Style.RESET_ALL)
        vstup = input(Style.BRIGHT + Fore.CYAN + "Zadej castku v EUR: " + Style.RESET_ALL)
        castka = int(vstup)
        result = z_eur_do_czk(castka, kurz_eur)
    else:
        castka = int(vstup)
        result = z_eur_do_czk(castka, kurz_eur)
elif exchange_type == 3:
    vstup = input(Style.BRIGHT + Fore.CYAN + "Zadej castku v CZK: " + Style.RESET_ALL)
    castka = vstup

    if not vstup.isdigit():
        print(Style.BRIGHT + Fore.RED + "Chybne zadana castka" + Style.RESET_ALL)
        vstup = input(Style.BRIGHT + Fore.CYAN + "Zadej castku v CZK: " + Style.RESET_ALL)
        castka = int(vstup)
        result = z_czk_do_usd(castka, kurz_usd)
    else:
        castka = int(vstup)
        result = z_czk_do_usd(castka, kurz_usd)
elif exchange_type == 4:
    vstup = input(Style.BRIGHT + Fore.CYAN + "Zadej castku v USD: " + Style.RESET_ALL)
    castka = vstup

    if not vstup.isdigit():
        print(Style.BRIGHT + Fore.RED + "Chybne zadana castka" + Style.RESET_ALL)
        vstup = input(Style.BRIGHT + Fore.CYAN + "Zadej castku v USD: " + Style.RESET_ALL)
        castka = int(vstup)
        result = z_usd_do_czk(castka, kurz_usd)
    else:
        castka = int(vstup)
        result = z_usd_do_czk(castka, kurz_usd)
elif exchange_type == 5:
    vstup = input(Style.BRIGHT + Fore.CYAN + "Zadej castku v USD: " + Style.RESET_ALL)
    castka = vstup

    if not vstup.isdigit():
        print(Style.BRIGHT + Fore.RED + "Chybne zadana castka" + Style.RESET_ALL)
        vstup = input(Style.BRIGHT + Fore.CYAN + "Zadej castku v USD: " + Style.RESET_ALL)
        castka = int(vstup)
        result = z_usd_do_eur(castka, kurz_eur, kurz_usd)
    else:
        castka = int(vstup)
        result = z_usd_do_eur(castka, kurz_eur, kurz_usd)
elif exchange_type == 6:
    vstup = input(Style.BRIGHT + Fore.CYAN + "Zadej castku v EUR: " + Style.RESET_ALL)
    castka = vstup

    if not vstup.isdigit():
        print(Style.BRIGHT + Fore.RED + "Chybne zadana castka" + Style.RESET_ALL)
        vstup = input(Style.BRIGHT + Fore.CYAN + "Zadej castku v EUR: " + Style.RESET_ALL)
        castka = int(vstup)
        result = z_eur_do_usd(castka, kurz_usd, kurz_eur)
    else:
        castka = int(vstup)
        result = z_eur_do_usd(castka, kurz_usd, kurz_eur)

print(Fore.CYAN + f"Vysledek je {result:.3f}" + Style.RESET_ALL)