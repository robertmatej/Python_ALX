def podzielna_przez_2(x):

    return x%2==0

print (podzielna_przez_2(12))
print (podzielna_przez_2(11))

y = lambda x: x%2 ==0      #funkcja definiowana w locie LAMBDA
y2 = podzielna_przez_2
print (y(2))
print (y2(2))


def wybierz(dane, warunek):
    out = []
    for element in dane:
        if warunek(element):
            out.append(element)

    return out


lista = [1,2,3,4,5,6,7,8]

print(wybierz(lista, podzielna_przez_2))
