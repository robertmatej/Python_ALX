def drukuj_linie():
    print ('-'*40)

def przyjmij_wartosc_wpisana ():
    wartosc = input('podaj wartość')
    return wartosc

#drukuj_linie()

#x= zwroc_wartosc_wpisana()

a= [1,2,3,4,5,6]

def sumator(a):
    x = [1, 2, 3, 4, 5, 6]

    return sum(a)

    print(locals())
    print(globals())


def kalkulator (a, b, operacja='+', opis=''):
    if opis:
        print(opis)
    if operacja== '+':
        return a+b
    elif operacja=='-':
        return a-b

print (kalkulator(1,3, '-',"takie tam liczenie"))
print (kalkulator(1,3,"takie tam liczenie")) #pprblem bo mysli ze 3 argument to dzialane