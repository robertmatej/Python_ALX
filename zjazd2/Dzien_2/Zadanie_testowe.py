def foo2(cena,*args, **kwargs):
    # print('args', args)
    # print('cena', cena)
    # print('kwaargs', kwargs)

    for text in args:
        print(text)

    for key in kwargs:
        print (text)



x= ['tekst 1 $cena','tekst 2 $cena','tekst 4 $cena']
slownik={'cena': 10, 'podatek': 0.23}

foo2(10,*x)

#foo2(x,'tekst1',10, 'text2')