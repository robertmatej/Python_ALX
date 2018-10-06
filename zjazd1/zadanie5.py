miastoA = input("podaj miasto A: ")
miastoB = input("podaj miasto B: ")
dystans2 = int(input(f"Podaj odległość midyz miastem {miastoA} a mistem {miastoB}: "))
dystans = 320

# rzutowanie


cena_paliwa = 4.55
cena_paliwa2 = float(input("Podaj cene paliwa: "))
spalanie = 5.5
spalanie2 = float(input("Podaj spalanie: "))
# print (miastoA)

koszt_przejazdu = int((dystans2 / 100) * spalanie2 * cena_paliwa2)
print(koszt_przejazdu)
output = f"Koszt przejazdu z {miastoA} do miasta {miastoB}\n wynosi: {koszt_przejazdu} PLN"

print(output)

output2= f'''
Miasto A: {miastoA}
Miasto B: {miastoB}
dystans: {miastoA} - {miastoB}: {dystans2}
cena paliwa: {cena_paliwa2}
spalanie 100km
Koszt przejazdu z {miastoA} do miasta {miastoB}\n wynosi: {koszt_przejazdu} PLN"

'''

print (output2)
