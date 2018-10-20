#wersja kolegi









#wersja wykladowcy
my_text = input('podaj napis: ')

czy_miedzy_nawiasami = False
licznik = 0

for znak in my_text:
    if znak=='<':
        czy_miedzy_nawiasami = True
    elif znak=='>':
        czy_miedzy_nawiasami = False

    elif czy_miedzy_nawiasami:   #jeżeli tu był if to wliczalo znaki <> do sumy
        licznik += 1

print (f'znaki w nawiasie {licznik}' )

