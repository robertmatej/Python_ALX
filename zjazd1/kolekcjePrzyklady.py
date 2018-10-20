'''
instalacja lepszego interpretera, lpesze wyswietlanie itp.
# pip install ipython

'''

napis = "Ala ma kota"

print(napis[2])
print(napis[4])

print (napis[0:4])
print (napis[::2])
print (napis[-1])


# for litera in napis:
#     print(litera)
#     print(litera)


ala=('A', 'l', 'a', ' ', 'm' 'a')

print (ala[0:5])

# wyszukiwanie elemtnu w tupli
print ('y' in ala)

# id wyciąga adres obiektu w pamięci
print(id(ala))

#tupla
a=('a', 1 ,4, 5 ,(3,2),'napis',8)
print (a[4])
print (a[4][1])

# range generuje do zzadanej wartosci licznik
for i in range(10):
    print(i)