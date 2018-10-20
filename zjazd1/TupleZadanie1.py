a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f'dlugosc tupli {len(a)}')
print(f'drugi el. {a[1]}')
print(f'przedost el. {a[-2]}')
print(f'od 3 do 7 włącznie el. {a[2:7]}')
print(f'co 3 el. {a[2:8:3]}')

print(f'co drugi od konca el. {a[::2]}')
assert (10, 8, 6, 4, 2) == a[::-2]

x = tuple()


# LISTA

lista1 =list()
lista2=[]
lista3=[1,2,3,4]
lista4= list((1,2,3, 'a'))

print(lista1)
print(lista2)
print(lista3)
print(lista4)

# dodanie elementu do dlisty
lista3.append(6)
print (lista3 )

#usuwanie elementu z listy
lista3.pop()
print(lista3)

