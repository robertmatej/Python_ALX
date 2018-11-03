'''
Gra w której gracz szuka skarbu na planszy 10x10

skarb i gracz na tym samym polu wygrywamu
wyjscie poza plansze przegywasz
losujemy położenie startowe gracz
losujemy położenie skarbu

za pomocą klawiatury porszamy graczem
obsługa klawiatury
w- gora
s - dół
a - lewo
d - prawo

po kjazdym kroku liczy odleglosc do skarbu
po odnalezieniu skarbu piszem ile ruchów to zajelo

okreslić minimalną liczbę krotków i po jej osiągniećiu przemieścić skarb

'''

from random import randint

def pobranie_rozmiaru_planszy():
    szerokosc = int(input('Podaj szerokosc planszy: '))
    wysokosc = int(input('Podaj wysyokość planszy: '))

    return szerokosc, wysokosc


def inicjowanie_pozycji(rozmiar_planszy_x, rozmiar_planszy_y):

    # pozycjonowanie skarbu
    xs = randint(1, rozmiar_planszy_x)
    ys = randint(1, rozmiar_planszy_y)
    print(f'Polożenie skarbu x: {xs}, y: {ys}')

    # pozycjonowanie gracza
    xg = randint(1, rozmiar_planszy_x)
    yg = randint(1, rozmiar_planszy_y)
    print(f'Rozpoczynasz grę z punktu x: {xg}, y: {yg}')

    return xs,ys,xg,yg


def obsluga_klwiatury (xg,yg):
    # obsluga klawiatury - poruszanie gracza po planszy
    # w - y zwiększa się
    # s - y zmnijsza się

    ruch = input('wykonaj ruch za pomocą przycisków: [wasd] : ')
    if ruch == 'w':
        yg += 1
    if ruch == 's':
        yg -= 1
    if ruch == 'a':
        xg -= 1
    if ruch == 'd':
        xg += 1
    return (xg,yg)

def podpowiedzi_po_wykonanu_ruchu (xs,ys,xg,yg):   #raczej samo infomrowanie o polozeniu
    # obliczenie odleglosci po ruchu
    min_odleglosc_po_ruchu= abs(xs - xg) + abs(ys - yg)
    #min_odleglosc_po_los = abs(xs - xg) + abs(ys - yg)
    if min_odleglosc_po_ruchu>odleglosc_od_skarbu_przed_los:
        print ('Zimno')
    if min_odleglosc_po_ruchu<odleglosc_od_skarbu_przed_los:
        print ('Ciepło')

    print(f'Polożenie gracza x: {xg}, y: {yg}')
    print(f'Odległość gracza od skarbu x: {min_odleglosc_po_ruchu}')

    return min_odleglosc_po_ruchu


def warunki_zakonczenia_gry(xg,yg, min_odleglosc_po_ruchu,rozmiar_planszy_x, rozmiar_planszy_y):
    flaga = 0
    #Warunki zakończneia gry po wyjsciu za plansze
    if xg>rozmiar_planszy_x or xg<1:
        print('GAME OVER jesteś poza planszą')
        flaga =1
    if yg> rozmiar_planszy_y or yg<1:
        print('GAME OVER jesteś poza planszą')
        flaga = 1
    #Wygrana
    if min_odleglosc_po_ruchu ==0:
        print('WYGRAŁEŚ')
        flaga = 1
    # powiekszam liczbe ruchow


    return flaga



# PROGRAM GŁÓWNY wykorzystywanie fuinkcji

rozmiar_planszy_x, rozmiar_planszy_y = pobranie_rozmiaru_planszy()
xs,ys,xg,yg = inicjowanie_pozycji(rozmiar_planszy_x, rozmiar_planszy_y)
licz_krok = 1
while True:

    # odleglosc minimalną odl. gracz - skarb przed ruchem
    odleglosc_od_skarbu_przed_los = abs(xs - xg) + abs(ys - yg)


    xg,yg = obsluga_klwiatury(xg,yg)
    odl_po_ruchu = podpowiedzi_po_wykonanu_ruchu(xs,ys,xg,yg)
    znacznik_zakonczenia = warunki_zakonczenia_gry(xg,yg,odl_po_ruchu, rozmiar_planszy_x, rozmiar_planszy_y)
    if znacznik_zakonczenia == 1:
        break
    licz_krok +=1

print(f'wykonałeś {licz_krok} kroków ')