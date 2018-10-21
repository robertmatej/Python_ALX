# V1 funkcja przyjmuje zmienną cena oraz nieokreśloną liczbę tekstów, w tytch tekstach trzeba zamienić $cena na
# na wartoiść zmiennej cena i zwrócić tekst w kazdej linii


def formatuj(cena,*args):
    out= []
    for text in args:
        text=text.replace('$cena',str(cena))
        out.append(text)
    return '\n'.join(out)     #łączy teksty znakiem nowej linii

def test_formatuj():

    assert formatuj(
                    10,
                    'koszt $cena PLN',
                    'kwota $cena brutto'
                    ) == "koszt 10 PLN\nkwota 10 brutto"



    assert formatuj(
                    10,
                    'koszt $cena PLN',
                    'kwota $cena brutto',
                    'sumarycznie $cena'
                    ) == "koszt 10 PLN\nkwota 10 brutto\nsumarycznie 10"