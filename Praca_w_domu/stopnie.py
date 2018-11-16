'''
Woda zamarza przy 32 stopniach Fahrenheita, a wrze przy 212 stopniach Fahrenheita.
 Napisz program "stopnie.py", który wyświetli tabelę przeliczeń stopni Celsjusza na
 stopnie Fahrenheita w zakresie od –20 do +40 stopni Celsjusza (co 5 stopni).
 Pamiętaj o wyświetlaniu znaku plus/minus przy temperaturze.
 [ºC]=([ºF]-32)*5/9

'''

stopnie_celsjusz = -20
stopnie_fahrenheit = None


while stopnie_celsjusz <= 40:
    stopnie_fahrenheit = stopnie_celsjusz*(9/5)+32

    print (f'{stopnie_celsjusz}[ºC]  -  {stopnie_fahrenheit}[ºF]')
    stopnie_celsjusz += 5