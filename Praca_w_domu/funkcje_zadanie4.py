'''
napisz funkcję zmieniającą dane napisy

'''

def formatuj(cena, *args):

    for te in args:
        tekst2 = te.replace("ja", "da")
        tekst2 = te.replace("%cena", str(cena))
        print (f'tekst po przerobce: {tekst2}')



assert formatuj(10,"jakie jakich tych i takich jak nie ja ja good %cena, jest to kosmiczna cena %cena", 'lol' ,'jajajajajaj') =="""jakie jakich tych i takich jak nie ja ja good 10 jest to kosmiczna cena 10
lol
jajajajajaj"""