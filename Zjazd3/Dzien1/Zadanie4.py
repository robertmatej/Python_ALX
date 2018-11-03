# implementacja metody Basketumożliwiającą doadanie porduktu do koszyka

class Product:

    def __init__(self, id, name, price):
        self.product_ID = id
        self.product_name = name
        self.product_price = price

    def print_info(self):
        return f'Produkt"{self.nazwa}", id: {self.id}, cena: {self.cena}'


class Basket(object):
    def __init__(self):
        self.position_on_list = None
        self.sum_ = 0

    def __str__(self):
        return "Basket"

def test_product_print_info():
    product = Product(1, 'Woda', 10.00)
    product.print_info ()== '1, 'Woda', 10.00'

def test_create_basket():
    basket = Basket()
    assert str(basket) == "Basket"
    assert basket.produkty == []

def add_produkt_to_basket():
    basket= Basket()
    basket.add_product(product,5)
    assert basket.count_total_price() == 50
    assert basket.generate_report() =='Produkty w koszyku: \n- Woda (1), cena: 10.00 x 5 \nW sumie: 50.00'


