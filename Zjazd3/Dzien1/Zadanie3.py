class ElectricCar():

    def __init__(self, zasieg):
        self.range = zasieg
        self.distance = zasieg
        # self.discharge = 0

    def charging(self):
        return self.range == 100


    def drive(self, km):
        self.range = self.range - km
        if km >self.range:
            print (f'Za mało baterii, naładuj. Zostało do przejechania: {self.range}')
            return self.range


#
# def test_car():
#     car = ElectricCar(40)
#     assert car.charge() == 100
#     #assert car () == 100

def test_car_drive():
    car = ElectricCar (100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30
    assert car.drive(30) == 0
    car.charge()
    assert car.drive(50) == 50