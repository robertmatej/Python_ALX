# V1 funkcja przyjmuje zmienną cena oraz nieokreśloną liczbę tekstów, w tytch tekstach trzeba zamienić $cena na
# na wartoiść zmiennej cena i zwrócić tekst w kazdej linii


def formatuj(a,b,*args,marker='*',**kwargs):
    out= []
    for text in args:
        for k in kwargs:
            text=text.replace(f'{marker}{k}',str(kwargs[k]))     #k - key klucz ze słownika
        out.append(text)
    return '\n'.join(out)     #łączy teksty znakiem nowej linii

def test_formatuj():

    assert formatuj(1,2,
                    'koszt cena PLN',
                    'kwota cena brutto',
                    cena = 10,
                    )=="koszt PLN\nkwota cena brutto"

    # assert formatuj(
    #                 10,
    #                 'koszt $cena PLN',
    #                 'kwota $cena brutto',
    #                 cena = 10,
    #                 )=="koszt 10 PLN\nkwota 10 brutto"
