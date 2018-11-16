'''
Zdefiniuj funkcję "geo", która dla podanych trzech parametrów: n=numer elementu ciągu,
a1=wartość pierwszego elementu ciągu (domyślnie 1),
q=wartość iloczynu ciągu geometrycznego (domyślnie 2) zwróci n-ty element ciągu geometrycznego.

an = a1*q^(n-1)
'''

import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])

else:
    n = 1

#n=5
print (f'n: {n}')
a1 = 1
q =2

an = a1*q**(n-1)

print (f'{n}-ty element ciągu geometrycznego wynosi: {an}')
