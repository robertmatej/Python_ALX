def wiecej_niz(napis, prog):
    licznik_liter ={}
    wynik = set ()
#zliczyc
    for litera in napis:
        litera = in napis:
        litera




    returm set()



#liczymy wystapienia x={"a": 3, "b":2}


#sprawdzić które liczniki są wieksze niż próg x['a'] > 2


#zwrócić gdzie są nadzmiary


# testy napisane trzeba zrobic program zeby przeszedl testy
def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz('', 0) == set()

def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz('aaaaabbbccd', 2) == {'a','b'}
