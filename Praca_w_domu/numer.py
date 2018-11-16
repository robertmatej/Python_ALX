'''
Napisz program "numer.py", który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową:

a) znaki nie będące cyframi mają być ignorowane

b) konwertujemy cyfry, nie liczby, a zatem:

- 911 to "dziewięć jeden jeden"

- 1100 to "jeden jeden zero zero"
'''

import sys
# ilosc_liczb = len(sys.argv)
wejscie = list()
lacznik = ' '
for inp in sys.argv:
    wejscie.append(inp)

wej_polaczone = lacznik.join(wejscie)
#print(wej_polaczone)
wyjscie = list()
j=0
space= ' '

for i in wej_polaczone:
    if i== '1':
        wyjscie.insert(j, 'jeden ')
        j+=1
    elif i== '2':
        wyjscie.insert(j, 'dwa ')
        j+=1
    elif i== '3':
        wyjscie.insert(j, 'trzy ')
        j+=1
    elif i== '4':
        wyjscie.insert(j, 'cztery ')
        j+=1
    elif i== '5':
        wyjscie.insert(j, 'pięć ')
        j+=1
    elif i== '6':
        wyjscie.insert(j, 'sześć ')
        j+=1
    elif i== '7':
        wyjscie.insert(j, 'siedem ')
        j+=1
    elif i== '8':
        wyjscie.insert(j, 'osiem ')
        j+=1
    elif i== '9':
        wyjscie.insert(j, 'dziweięć ')
        j+=1
    elif i== '0':
        wyjscie.insert(j, 'zero ')
        j+=1
    # else:
    #     wyjscie.insert(j, '%')
    #     j += 1

print(space.join(wyjscie))