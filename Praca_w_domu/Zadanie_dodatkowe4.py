"""
Program wczytujący od usera liczbę X
nastepnie rysuje romb o wysokości 2 X


"""

wejscie = int(input('Podaj luczbę wyrysujemy romb o podwojonej wys.: '))
i = 0
i_malej = 2 * wejscie
spacja = ' '
while i <= 2 * wejscie:
    if i == 0:
        print(f'{i_malej*spacja}/\\')
    elif i == (2 * wejscie):
        print(f'{i*spacja}\\/')
    elif i < wejscie:
        print(f'{i_malej*spacja}/{i*2*spacja}\\')
    elif i > wejscie:
        print(f'{i*spacja}\\{i_malej*2*spacja}/')

    i += 1
    i_malej-=1
