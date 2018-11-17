'''
Napisz program obslugujący bazę danych pracownikow. w bazie danych przechowuj imię , nazwisko,
e-mail, rok urozdzeni, pensję.
skorzystać z JSON
przykład

python_employees.py
co chesz zrobić? [d - dodaj], w - wypisz] d
Imie: Jan
Nazwisko: Nowak
Rok urodzenia 1980
Pensja: 5000.0

python_emloyees.py
Co chesz zrobic............... [] w
Pracownicy:
- [1] Jan nowak rok urzodzenia 1980, pensja: 5000.00 PLN

'''


import json

while True:
    czynnosc = input('Co chesz zrobić? [d - dodaj, w - wypisz, q - wyjdz] ')

    try:                                    # prubujemy coś zrobić jak nie to...
        with open('pracownicy.json') as f:
            pracownicy = json.load(f)
    except FileNotFoundError:               # jak się nie uda to rób:....
        pracownicy=[]
    else:
        pass
    finally:                                # poinno zadziać się ostateczieto....
        pass

    if czynnosc == 'd':
        imie = input('Podaj imie: ')
        nazwisko = input('Podaj nazwisko: ')
        rok = input('Podaj rok urodzenia: ')
        zarobki = input('Podaj zarobki: ')

        pracownik = {'Imie': imie, 'Nazwisko':nazwisko,'Rok urodzenia': rok, 'Zarobki': zarobki}
        pracownicy.append(pracownik)
        with open("pracownicy.json", "w") as f:
            json.dump(pracownicy, f)

    if czynnosc == 'w':
        print('Pracownicy')
        for i,pracownik in enumerate(pracownicy, start =1):
            print(f"- [{i}] {pracownik['Imie']} {pracownik['Nazwisko']} - rok: {pracownik['Rok urodzenia']} {pracownik['Zarobki']}")

    elif czynnosc == 'q':
        print('Koniec programu')
        break

    else:
         print('Podaj [d] bądź [w] lub [q]')


# problem przy wybraniu w - wypisania, ie zgadza sie paramert imi - niby taki sam ??