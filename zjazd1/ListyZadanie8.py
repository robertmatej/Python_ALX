# program liczy liczbę znaków podanyhch w napisie przez użytkownika <>, nawias może być tylko jeden

print ('program policzy ile znaków jest wpisanych pomiędzy <>, nawias może wystąpić raz')



q='a'
while q!='q':
    iter=0
    licz = 0
    napis = input('Proszę wprowadź napis z <> w ciągu: ')
    for test in napis:
        if test == '<':
            while test != '>':
                test = napis[iter]
                iter += 1
                licz+=1

        iter += 1

    print(f'liczba znaków w nawiasie <> wynosi: {licz-2}')
    q = input('Czy zakończyuć program, wciśnij q aby zakończyć: ')