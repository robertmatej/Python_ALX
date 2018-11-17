class ElectricCar():

    def __init__(self, zasieg):
        self.range = zasieg
        self.possible_distance = zasieg
        # self.discharge = 0

    def charging(self):
        self.possible_distance =  self.range


    def drive(self, distance):
        if distance >= self.possible_distance:
            can_travel = self.possible_distance
            self.possible_distance = 0
            return can_travel

        self.possible_distance -= distance
        return distance


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
    car.charging()
    assert car.drive(50) == 50
