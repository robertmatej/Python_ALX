# implementacja metody Basketumożliwiającą doadanie porduktu do koszyka

class Product:

    def __init__(self, id, name, price):
        self.product_ID = id
        self.product_name = name
        self.product_price = price

    def print_info(self):
        return f'Produkt"{self.product_name}", id: {self.product_ID}, cena: {self.product_price}'

class BasketEntry:
    def __init__(self,product, quantity):
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.product_price*self.quantity



class Basket(object):
    def __init__(self):
        self.position_on_list = None
        self.sum_ = 0

    def add_product(self,product, quantity):
        self.entries.append(product,quantity)

    def __str__(self):
        return "Basket"

    def count_total_price(self):
        sum= 0
        for e in self.fentries:
            sum+=e.product.price*e.quantity
        return sum

def test_product_print_info():
    product = Product(1, 'Woda', 10.00)
    product.print_info ()== 1, 'Woda', 10.00

def test_create_basket():
    basket = Basket()
    assert str(basket) == "Basket"
    assert basket.entries == []

def test_add_produkt_to_basket():
    basket= Basket()
    product = Product(1, 'woda',10)
    basket.add_product(product,5)

def test_basket_enntry_count_price ():
    be=BasketEntry(Product(1,"Woda",2),5)
    assert be.count_price() == 00


def test_basket_count_total_price ():
    basket = Basket()
    product = Product(1, 'woda',10)
    basket.add_product(product,5)
    assert count_total_price() == 50

def test_basket_generate_report():
    assert basket.generate_report() == 'Produkty w koszyku: \n- Woda (1), cena: 10.00 x 5 \nW sumie: 50.00'


#    assert len(basket(entries)) == 1
