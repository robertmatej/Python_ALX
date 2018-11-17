class Animal:

    nazwa = 'Fauna' #atrybut klasowy, dotyczą całej klasy
    licnzik = 0

    def __init__(self, gatunek):    #self to tylko zwyczajjowa nazwa może być inne słowo
        self.gatunek=gatunek        #atrybuty instancji / obiektu
        #self.imie = imie
        #self.licznik +=1
        #licznik +=1
        self.stan="nic nie robi"
        self.pasza = None


    def __str__(self):
        return "Animal"

    def idz(self):
        self.stan='Idzie'

    def spij(selfself):
        self.stan = 'śpi'

    # @classmethod        #dekorator
    # def zwieksz_licznik(cls):
    #     cls.licznik+=1


class leniweZwierzeta(Animal):

    def idz(self):
        self.stan = "leży"
        print('Chyba żartujesz')

#tworzenie instancji danej klasy
azor = Animal("Canis Familiaris")
rudolf= Animal("")
garfield/leniweZwierzeta("Catus Felis")
# print(azor)
# print (type(azor))
# print (dir(azor))

print(azor)    #reprezentacja napisaow mojej instancji
print(azor.nazwa)       #wypisyanie atryubutu
print(azor.gatunek)

#print(Animal.licznik)