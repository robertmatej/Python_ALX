
produkty = {'koper': 13, 'piwo': 4, 'fasola': 5, 'pomarancze': 4, 'siemnikaki': 3}
magazyn = {'koper': 10, 'piwo': 50, 'fasola': 15, 'pomarancze': 15, 'siemnikaki': 30}

lista_zakupow = {'koper': 0.1, 'piwo': 2}

do_zaplaty=0
while True:
    print ('Nasz zelnik oferuje')
    for produkt in produkty:

        print(f'- {produkt} - {produkty[produkt]}PLN')
    print('')
    komenda = input('Co chesz zrobić k[kupic], d[dodac] [koniec] aby wyjsc: ')
    if komenda == 'koniec':
        break

    produkt_wybrany=input('co chcesz kupic?: ')
    if produkt_wybrany not in produkty:
        print('nie mamy takiego produktu')
        continue
# zdjecei z magazynu
    if magazyn[produkt_wybrany]<waga:
        print(f'mamy za mało tego {produkt_wybrany}, pozostało {magazyn[produkt wybrany]}kg ')
        continue
    magazyn[produkt_wybrany]=magazyn[produkt_wybrany] - waga

    waga= float(input(f'ile chcesz kupić wybranego produktu [{produkt_wybrany}]: '))
    cena = produkty[produkt_wybrany]
    koszyk[produkt_wybrany] += koszt
# dodanie do magazynu
    elif komenda == 'd':
        produkt_do_dodania = input ('jaki produkt chesz dodoac? ')
        if produkt_do_dodania not in magazyn:
            magazyn[produkt_do_dodania] = 0
            cena_nowego_produktu = float(input(' Za ile sprzedajemy'))
            produkt_do_dodania = cena_nowego_produktu

        ile_produktu_dodajemy = float(input("Ile produktu dodać "))
        magazyn[produkt_do_dodania] += ile_produktu_dodajemy
    else:
        ('komenda nie poprawna'):


    #for produkt in produkty:


    koszt = waga*cena
    do_zaplaty += koszt

print(f'do zaplaty: {do_zaplaty}')
for produkt in koszyk:
    print(f' - {produkt} - {koszyk[produkt]}PLN ')
    suma += koszyk[produkt]

print (' - '*40)
print (f'Suma: {suma} PLN ')