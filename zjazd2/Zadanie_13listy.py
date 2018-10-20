

kwadraty = {(x, x**2) for x in range(1,100)}

pkt2 = {(x, x**3, x**3) for x in range(1,100)}

zbior_napisow = {'abc', 'ala ma kota', 'Słowacki wielkim poeetą', "superman"}

kwadraty = []
for x in range(1,101):
    kwadraty.append(x**2)

print(kwadraty)

print(pkt2)
print({x:len(x) for x in zbior_napisow})

print([x for x in range(1,100)if x%3==0])