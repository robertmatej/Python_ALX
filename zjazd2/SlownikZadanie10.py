# liczy wystąpienie każdego znaku w napisie od usera

napis= input ('Wpsisz napis do zliczenia znakow:  ')
licznik_liter = {}

# zliczyć
for litera in  napis:
    # if litera in licznik_liter:
    #     licznik_liter[litera]+=1
    # elif:
    #     licznik_liter[litera] = 1
    licznik_liter[litera]=licznik_liter.get(litera, 0)+1
#wyświetlić


for litera in licznik_liter:
    print (f'litera: {litera} wystąpiłą {licznik_liter} razy: ')

    #licznik_liter = {litera: 1}

    #print(licznik_liter)

