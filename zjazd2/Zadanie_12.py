liczby = [5,2,1,4,3]

print('Przed: ', liczby)

for i in range(len(liczby)):
    index_min = i
    print('i ',i,'Liczby ',liczby[i:])
    for j in range(i+1, len(liczby)):
        if liczby[j] < liczby[index_min]:
            index_min = j
    liczby[i], liczby[index_min] = liczby[index_min], liczby[i]

#liczby[0], liczby[4] = liczby[4],liczby[0]
print('Po: ', liczby)