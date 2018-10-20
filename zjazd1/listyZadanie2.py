"""
Program obliczający średnią wartość z podanych przez Usera
do przechowaniaaliczb uzyć listy
max licba wprowadzeń to 10
skoerzystać z funkcji sum()
"""

wejscie= []
licznik=0
len_liczby =10

while licznik<10:
    #pobranie danyc do tabeli w pętli
    wejscie.append(input(f'Podaj liczbe nr {licznik+1}: '))
    licznik += 1
else:
    # warunek max 10 liczb
    print ('wprowadzileś maksymalną ilość liczb')
#    break

srednia = sum(wejscie)/len(wejscie)
print(f'Srednia z wprowadz liczb to: {srednia}')
