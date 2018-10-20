#
def czy_jest_pierwsza(liczba):
    dzielna = range(1, liczba)
    for i in dzielna:

        if liczba % i == 0:
            print ('Twoaja liczba NIE jest pierwsza')
            break

        else:
            print('twoja licza jest pierwsza')

        return True

wejscie = int(input('Podaj liczbę do testów: '))
czy_jest_pierwsza(wejscie)
