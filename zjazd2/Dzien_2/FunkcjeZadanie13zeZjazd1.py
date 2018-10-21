def pobrnaie_temperatur ():
    dni = int(input('dla ilu dni podajesz temperaturę: '))
    temperatura = []
    for i in range(dni):
        temp = int(input(f'podaj tepmeraturę dla dnia {i}: '))
        temperatura.append(temp)
    print(temp)
    return  temperatura



def licz_srednia_temperatur (temp):
    srednia = sum(temp) / len(temp)
    return srednia


def wyswietlanie(temperatura):
    return print(f'średnia temperatura z {len(temp)} dni to {srednia}: ')    #dlczego lan(temp) dziala a temperatura nie

temp = pobrnaie_temperatur()
srednia = licz_srednia_temperatur(temp)
wyswietlanie(srednia)