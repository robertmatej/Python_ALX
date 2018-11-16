''''
Napisz program "login.py", który wczyta od użytkownika login i hasło.
Jeżeli w słowniku haseł znajduje się odpowiedni login i hasło,
program powinien wyświetlić „Autoryzacja pomyślna”; inaczej – „Błąd logowania”.

'''

import sys
flaga = 0
slownik = {'a.matejek':'ania12', 'r.matejek': 'robert12', 'k.ancerowicz': 'krzysiek12', 'a.kosmatka':'aga12', 'lol': 'lol'}
if len(sys.argv)>2:
    login = sys.argv[1]
    haslo = sys.argv[2]
    for spr in slownik:
        if spr == login and slownik[login] == haslo:
            flaga = 1
else:
    print ("nie wprowadzono loginu lub hasła")


if flaga ==1:
    print('Autoryzacja pomyślna ')
else:
    print('Błąd logowania ')