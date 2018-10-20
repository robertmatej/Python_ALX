# napis = 'to jest napis'
#
# for litera in napis:
#         print(litera)
#
# #print(dir(napis))
#
#
# #Słowniki

my_dict={
    "pierwsza": 'a',
    'druga': 'b'
}

my_dict['terzecia']='c'
d2 = dict([])
d2 = dict([('a',1),('b',2)])

produkt1 = {'nazwa': 'kasza','cena': 3}
produkt2 = {'nazwa': 'koper','cena': 1.99}

produkty = [produkt1, produkt2]
print(my_dict['pierwsza'])

print (type(my_dict))
print (dir(my_dict))
print (my_dict.items())
print (my_dict.keys())
print (my_dict.values())

print('produkty w lodówce')
for p in produkty:
    print(p['nazwa'])