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


# pozycjonowanie skarbu
xs = randint(1, 10)
ys = randint(1, 10)
print(f'Polożenie skarbu x: {xs}, y: {ys}')


# pozycjonowanie gracza
xg = randint(1, 10)
yg = randint(1, 10)
print(f'Polożenie gracza x: {xg}, y: {yg}')


# i = 0
# while i <= 10:
#     x = randint(0, 10)
#     y = randint(0, 10)
#
#     print(x)
#     i += 1



# obsluga klawiatury - poruszanie gracza po planszy
# w - y zwiększa się
# s - y zmnijsza się
licz_krok = 0
while True:
    # odleglosc minimalną odl. gracz - skarb przed ruchem
    min_odleglosc_po_los = abs(xs - xg) + abs(ys - yg)
    print(f'Odległość gracza od skarbu x: {min_odleglosc_po_los}')


    ruch = input('wykonaj ruch [wasd] : ')
    if ruch == 'w':
        yg += 1
    if ruch == 's':
        yg -= 1
    if ruch == 'a':
        xg -= 1
    if ruch == 'd':
        xg += 1

    # obliczenie odleglosci po ruchu
    min_odleglosc_po_ruchu= abs(xs - xg) + abs(ys - yg)
    if min_odleglosc_po_ruchu>min_odleglosc_po_los:
        print ('Zimno')
    if min_odleglosc_po_ruchu<min_odleglosc_po_los:
        print ('Ciepło')

    #zakończneie gry po wyjsciu za plansze
    if xg>10 or xg<1:
        print('GAME OVER jesteś poza planszą')
        break
    if yg>10 or xg<1:
        print('GAME OVER jesteś poza planszą')
        break
    #wygrana
    if min_odleglosc_po_los ==0:
        print('WYGRAŁEŚ')
        break
    # powiekszam liczbe ruchow
    licz_krok += 1

    print(f'Polożenie gracza x: {xg}, y: {yg}')
    # odleglosc minimalną odl. gracz - skarb
    min_odleglosc_po_los = abs(xs-xg)+abs(ys-yg)

    # przemieszczeie skarbu po x krokach

print(f'Odległość gracza od skarbu x: {min_odleglosc_po_los}')
print(f'wykonałeś {licz_krok} kroków ')