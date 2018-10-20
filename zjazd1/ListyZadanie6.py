liczby = [5,2,1,4,3]

min_i = None
max_i = None
temp = None
#Buf_max = None

print(liczby)
print(list(range(len(liczby))))
print(liczby[2]<liczby[3])
indeks=range(len(liczby)) #zwróciu infdeks z listy

for i in indeks:
    if min_i==None or liczby[i]<liczby[min_i]:
        min_i=i
    if max_i==None or liczby[i]>liczby[max_i]:
        max_i=i

   # print(i)
    #print(f'index najwiekszej liczby {max_i} ')
   # print(f'index najmnijeszej liczby {min_i} ')

#zamiana miejscami prosta z buforem

# temp = liczby[min_i]
# liczby[min_i]=liczby[max_i]
# liczby[max_i]=temp
#
# print (liczby)

# sposób 2 którtszy
liczby[min_i], liczby[max_i]= liczby[max_i], liczby[min_i]
print (liczby)

'''
buf = None

for i in liczby:
    buf=liczby(1)
    if buf<liczby(i):
        buf=liczby(i)
        pozycja_max = i
'''
# testowanie poprawnośći
assert liczby== [1,2,5,4,3]