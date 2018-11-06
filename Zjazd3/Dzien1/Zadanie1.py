

class Produkt:

    def __init__(self, id, nazwa, cena):
        self.ID = id
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        return f'Produkt"{self.nazwa}", id: {self.id}, cena: {self.cena}'


#lista = Produkt("Zakupy")




def test_produkt():
    produkt = Produkt(1, 'Woda', 10.99)
    assert produkt.ID == 1
    assert produkt.nazwa == 'Woda'
    assert produkt.cena == 10.99

#def test_produkt_info():
