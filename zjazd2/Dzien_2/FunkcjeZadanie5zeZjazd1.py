def pobieranie_danych():
    miasto_a = input("podaj miasto A: ")
    miasto_b = input("podaj miasto B: ")
    dystans = int(input(f"Podaj odległość midyz miastem {miasto_a} a mistem {miasto_b}: "))
    cena_paliwa = float(input("Podaj cene paliwa: "))
    spalanie = float(input("Podaj spalanie: "))

    return miasto_a , miasto_b , dystans, cena_paliwa, spalanie

def obliczanie_kosztu(dystans, spalanie, cena_paliwa):
    koszt_przejazdu = int((dystans / 100) * spalanie * cena_paliwa)
    return koszt_przejazdu

def drukuj_wynik():
    koszt_przejazdu = int((dystans / 100) * spalanie * cena_paliwa)
    output2 = f'''
       Miasto A: {miasto_a}
       Miasto B: {miasto_b}
       dystans: {miasto_a} - {miasto_b}: {dystans}
       cena paliwa: {cena_paliwa2}
       spalanie 100km
       Koszt przejazdu z {miasto_a} do miasta {miasto_b}\n wynosi: {koszt_przejazdu} PLN"

       '''
    return output2

dane= pobieranie_danych()
print(drukuj_wynik(*dane))

# print(koszt_przejazdu)
# output = f"Koszt przejazdu z {miastoA} do miasta {miastoB}\n wynosi: {koszt_przejazdu} PLN"

# print(dane)
# print(type(dane))
# koszt = obliczanie_kosztu(dane)

# # taki sam zapis * rozpakowuje np. tuple
# koszt = obliczanie_kosztu(*dane)
# koszt = obliczanie_kosztu(dane[0],dane[1],dane[2],dane[3])
