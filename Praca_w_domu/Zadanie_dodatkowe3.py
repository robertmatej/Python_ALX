'''
Program wczyta od Usera jakąś liczbę i narysuje kwadrat z gwiazdek o boku długości wprowadzonej liczby
'''
i = 0
dlugosc_boku = int(input("Podaj długość boku kwadratu: "))
znaczek= input('Podaj znak jakim będzie rysowany kwadrat: ')
while i <dlugosc_boku:
    # j == 1 bo pierwszy znak ryzuje pętla z i
    j=1
    while j <dlugosc_boku:

        if (i==0 or i==dlugosc_boku-1):
            # drukowanie poziome
            print(f'{znaczek}',end='')

        elif i > 0 and i < (dlugosc_boku - 1) :
            if j==1:
                print(f'{znaczek}', end='')
            else:
                print(' ', end='')
        j+=1
    #drukowanie pionowe
    print(f'{znaczek}', sep='Y', end="\n")
    i+=1
