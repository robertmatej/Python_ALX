'''

Napisz program "prk.py", który obliczy wszystkie pierwiastki rzeczywiste
równania kwadratowego o postaci ax2+bx+c=0, gdzie a, b i c podaje użytkownik.
Program powinien na początku sprawdzić, czy
wprowadzone równanie jest rzeczywiście kwadratowe.
'''


import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])


while True:
    if a == 0:
        print('Podałeś niewłaściwe parametry pierwszy argument nie może być 0, nie jest to rownanie kwadratowe ! ')
        break

    delta= b**2 - 4*a*c

    if delta < 0:
        print('Równanie nie ma pierwiastkó rzeczywistych')
        break

    elif delta == 0:
        x = -b/2*a
        print (f'Równanie ma jedno rozwiązanie: x: {x}')
        break
    elif delta > 0:
        x1 = (-b-math.sqrt(delta))/2*a
        x2 = (-b+math.sqrt(delta))/2*a
        print(f'Równanie ma dwa rozwiązania x1: {x1} oraz x2: {x2}')
        break
