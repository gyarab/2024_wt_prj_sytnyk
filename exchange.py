import httpx

print("Online prevodnik men dle cnb")

url = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt;jsessionid=5EBE7E79ED83B35877829238E5BBB94D?date=13.02.2025'

r = httpx.get(url)

#print(r.text)

in_array = r.text.split("\n")
#print(in_array)

for line in r.text:
    if "|EUR|" in line:
        print(line)

castka = input("Zadej castku v CZK: ")
result = int(castka) * 25
print(f"To je v EUR: {result}")