''''
program zlicza liczbę liczb ujemnych i dodatnich w zadanej liście liczb calkowitych

'''

lista = [-1, 2, -2,6,3 -4, 5, 5, -8, -8, 9]


#wersja licznik
dodatnie = 0
ujemne = 0

for licznik in lista:
    if lista[licznik] > 0:
        dodatnie +=1

    if lista[licznik] < 0:
        ujemne += 1

print (f'Liczb dodatnich jest: {dodatnie}, a ujemnyhc {ujemne}')

#wersja na listach
dodatnie = []
ujemne = []
for licznik2 in lista:
    if lista[licznik] > 0:
        dodatnie.append(licznik2)

    if lista[licznik] < 0:
        ujemne.append(licznik2)

print (f'Liczb dodatnich jest: {dodatnie}, a ujemnyhc {ujemne}')

print (f'Liczb dodatnich jest: {len(dodatnie)}, a ujemnyhc {len(ujemne)}')