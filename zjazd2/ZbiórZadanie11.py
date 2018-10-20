print(set([1,2,3,4,5,1]))

print(set(range(2,10)))

# wprowadza liczby do zbioru / unikalne
wejscie = set(input('podaj liczby'))

#genereuje liczby parzyste do poruwnania iuloczynem
liczby_100 = set(1,2,3,4,5,6)
parzyste = set()
for liczba in liczby_100:

    print ( set(range((1, 100))))
    if (liczba%2) == 0:
        parzyste.add(liczba)


# iloczyn zbiory
iloczyn = parzyste & wejscie


# liczy ile parzystych we wprowadzonych

print (f'wprowadzono {len(iloczyn)} parzystych liczb: ')