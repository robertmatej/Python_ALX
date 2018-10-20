# progmra wyświetla min i max z liczb wprowadzonycjh przez usera user moze3 zakonczyc wpraowadznanie dowolna komopnda
# obsłuyzyć niewprowadzenie zadnej liczby
# dodac srednią z wprowadzoinych

znal_max = None
znal_min = None

# ilosc = none
# liczba = print(f'podaj liczbę nr x do przeszukania: ')

while True:
    dane_we = input('podaj liczbę lub wpisz q by zakończyć: ')

    if dane_we == "q":
        break
    liczba = int(dane_we)

    if znal_max is None or liczba > znal_max:
        znal_max = liczba

    if znal_min is None or liczba < znal_min:
        znal_min = liczba


if not znal_max:
    print('Nie wprowadono danych')
else:
    print(f'Minimum {znal_min} Maximum {znal_max}')


print(f'Wprowadz liczbę nr x aby zakonczyć wprowadzanie naciśnij q ')
