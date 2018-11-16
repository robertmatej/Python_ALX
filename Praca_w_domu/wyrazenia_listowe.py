baza = {'login': 'haslo', 'dom': ' klucz', 'sejf': 'szyfr'}

print (baza.keys())

print (baza.values())
dane = baza.items()
print (dane)
print (baza.items())


lista = [a*0.1 for a in range(0, 11)]
print (lista)


# tuple w zbiorze
lista1 =range(-10,10)

lista2 = {tuple(range(-10,10)), tuple( a**2 for a in range(-10,11)), tuple(a**3 for a in lista1)}
print(lista2)

#Słownik ze zbioru napisów, mapuje napisy na ich długość

slownik = {"jaka jatka",'Będą jaja', 'jak źle policzy'}
#slownik_wynikowy = dict()
slownik_wynikowy = { (( k+2 for k in range(0,5) )):len(v) for (v) in {"jaka jatka",'Będą jaja', 'jak źle policzy'}}
#nie wiem jak ropakować klucz na wyjściu rzuca : <generator object <dictcomp>.<genexpr>

# wersja wieloliniowa:
#j=1
# for i in slownik:
#     slownik_wynikowy [j] = (len(i))
#     j+=1\

print(type(slownik_wynikowy))
print(slownik_wynikowy)