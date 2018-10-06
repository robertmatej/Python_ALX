wejscie = int(input("podaj liczbe do porownania: "))

"""czy liczb jest podzielna przez 2
podizelna przez 3
i wieksza od 10 
lub czy jest to liczba 7
"""
porzelna_przez2 = wejscie % 2 == 0
porzelna_przez3 = wejscie % 3 == 0
wieksza10= wejscie >10
rowna7 = wejscie==7
print (porzelna_przez2,porzelna_przez3,wieksza10,rowna7)

wynik = (porzelna_przez2 and
         porzelna_przez3 and
         wieksza10) or rowna7
print (wynik)

wynik2 = porzelna_przez2 and \
         porzelna_przez3 and \
         wieksza10 or rowna7
print (wynik2)


'''
# war1 = wejscie%=2 and
print(f"""
czy liczb jest podzielna przez 2: {(wejscie%2==0,and wejscie%3==0, and wejscie >10) or wejscie==7 },
podizelna przez 3
i wieksza od 10 
lub czy jest to liczba 7
""")
'''