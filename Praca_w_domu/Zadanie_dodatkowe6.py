"""
Porgram ryzujący trójkąt prosokątny o zadanej długości boku

"""

dlugosc_przyprostokatnej = int(input('Podaj dłuygośc przyprostokątnej: '))
spacja = ' '
gwiazdka = '*'
i = 0
while i < dlugosc_przyprostokatnej:

    if i == 0:
        print('*')
    elif i > 0 and i < dlugosc_przyprostokatnej-1:
        print(f'*{spacja*i}*')

    elif i == dlugosc_przyprostokatnej-1:
        print(dlugosc_przyprostokatnej * gwiazdka)

    i += 1
