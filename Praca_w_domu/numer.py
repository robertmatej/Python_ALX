'''
Napisz program "numer.py", który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową:

a) znaki nie będące cyframi mają być ignorowane

b) konwertujemy cyfry, nie liczby, a zatem:

- 911 to "dziewięć jeden jeden"

- 1100 to "jeden jeden zero zero"
'''

import sys

wejscie = sys.argv[1]
wyjscie = list()
j=0
for i in wejscie:
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
    # elif i==' '
    #     j+=1

print(wyjscie)