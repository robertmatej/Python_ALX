import json
import urllib.request

with urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/a?format=json") as f:
    print(f)
    kursy = json.loads(f.read())

rates = kursy[0]['rates']
print (rates)
for r in rates:
    print(f"- {r['code']} - {r['mid']}")

waluta = input('jaka waluta z listy: ')
ile = float(input('Ile wymieniasz? '))

for r in rates:
    if r['code']== waluta:
        result = ile* r['mid']

print (f"musisz zaplacić: {result}")

#kursy ={"trelemorele"}
#kursy = json.loads(kursy)

# print(json.loads(kursy))
