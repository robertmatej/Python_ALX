import json

# tworzę pythonowy obiekt

meble = ['krzeslo', 'szafa', 'komoda', 'stol']

print (type(meble))

meble_as_json = json.dumps(meble)

print(type(meble_as_json))
print(meble_as_json)


odczytane_z_jsona_meble = json.loads(meble_as_json)
print(type(odczytane_z_jsona_meble))
print(odczytane_z_jsona_meble)

with open ('meble.json', 'w') as f:
    json.dump (meble, f)        # dumpo potrzebuje obiektu który się serialuje i pliku gdzie zapisze
                                # spodziewa się ze będize praca na pliku

with open('meble.json') as f:
    meble = json.load(f)
    print(meble)                # w tym momencie zwracany jest obiek pythonowy

with open('meble.json') as f:
    meble2 = json.load(f)
    meble2.append('taboret')

print (meble2)

with open("meble2.json", 'w') as f:
    json.dump (meble2, f)       # nadpisuje plik dltego zrobilem nowy, nie dodaje nowych linii tylko caly plik nadpisuje


