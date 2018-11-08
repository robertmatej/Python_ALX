'''
User wprowadza tekst i zostaja obramowany gwiazdkami

'''

wejscie = input('Podaj tekst to zrobimy z niego gwiadę: ')
dlugosc_ramki = len(wejscie)+6
print (dlugosc_ramki*'*')
print(f'*  {wejscie}  *')
print(dlugosc_ramki* '*')