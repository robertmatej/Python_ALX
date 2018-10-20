'''
prog wypisuje all liczby opd 0 do 100 podizelne przez 3 lub przez 5
ile byloi takichj loiczb w przedziale
'''

podzielna = 0
wynik= []
#utworzenie listy 0-100  range(100), krok nie jest konieczny
lista=list(range(100))


for el in lista:
    if el%3==0 or el%5==0:
        wynik.append(el)


#wersjaalternatywna
for i in range(101):
    if i%3== 0 or i%5== 0:
        podzielna +=1

#wypisanie
print('liczby podizelne przez 3 lub 5')
for el in wynik:
    print(el)

print (f'podzielne przez 3 i 5 wer. wykladowcy {wynik} ')

print (f'podzielne przez 3 i 5 {podzielna} ')
