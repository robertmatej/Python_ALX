'''
Stwodrz klasę DOG wg. specuyfikacji:
1 piesz zużywa energię szczekając "bark
2 zyskuje energie spiac 'sleep'
3 pies ma poczatkowa 10 jednostek energii
4 pies ma metodę "get_energi ktora zwaraca  wartosc aktualnej energii"

'''

class Dog:

    nazwa = 'Burek'

    def __init__ (self):
        self.energy = 10
        # self.bark -=1
        # self.slep +=1
        # self.get_energy = 10

    def get_energy(self):
        return self.energy

    def bark(self):
        self.energy -=1

    def sleep(self):
        self.energy +=1

dog=Dog()
imie = dog("Azor2")



assert dog.get_energy() == 10
dog.bark()
dog.bark()
assert dog.get_energy() = 8
dog.sleep()
dog.sleep()
assert dog.get_energy() = 10

