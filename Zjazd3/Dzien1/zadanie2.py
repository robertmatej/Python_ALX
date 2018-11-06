'''
Obiektowe zadanie 2 z
klasa Employee rejestrująca rejestrowanie czasu pracy...


'''
class Employee:

    def __init__ (self, imie, nazwisko, stawka):
        self.name = imie
        self.surname = nazwisko
        self.hour_pay = stawka
#       self.salary = 0
        self.worked_hour = 0
        self.overhours = 0


    def pay_salary(self):
        to_pay = self.worked_hour*self.hour_pay
        self.worked_hour = 0
        return to_pay

    def register_time(self, hours):
        self.worked_hour = hours




def test_employee():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.name == 'Jan'
    assert employee.surname == 'Nowak'
    assert employee.hour_pay == 100


def test_employee_pay_salary_with_no_worked_hours():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.pay_salary() == 0


def test_employee_pay_salary_with_worked_hours():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary () == 500

def test_employee_pay_salary_after_salary_was_payed():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary() == 500
    assert employee.pay_salary() == 0


# PremiumEmployee

class PremiumEmployee(Employee):

    def __init__(self):             #nadpisałem poprzednią metodę init i wszsytko przepadło co tam mieliśmy ( w sensie ze nie dostepne w tej funkcji
        super().__init__(imie,nazwisko,stawka)
        self.bonus = 0

    def give_bonus(self,ammount):
        self.bonus = ammount


def test_PremiumEmployee():
    employeePremium = PremiumEmployee('Jan', 'Nowak', 1000.0)
    assert employeePremium.name == 'Jan'
    assert employeePremium.surname == 'Nowak'
    assert employeePremium.hour_pay == 1000

def test_premium_employee_pay_bonus():
    employeePremium = PremiumEmployee('Jan', 'Nowak', 1000.0)
    assert employeePremium.name == 'Jan'
    assert employeePremium.surname == 'Nowak'
    assert employeePremium.hour_pay == 1000

def test_premium_employee_pay_without_bonus():
    employeePremium = PremiumEmployee('Jan', 'Nowak', 1000.0)
    assert employeePremium.name == 'Jan'
    assert employeePremium.surname == 'Nowak'
    assert employeePremium.hour_pay == 1000



#utwórz klasę Company, kórą inicjalizuje się z nazwą
# wywołania konsoli:
# >>> employee = Employee('Jan', 'Nowak', 1000.0)
# >>> employee.register_time(5)
# >>>google = Company('google')
# >>>google.add_employee(employee)
# >>> google.size()
#>>> 1
# google.pay_all_salary()
#  0
# employee2 = =Employee('Krzysztof', 'Nowak', 200.0')
# employee2.register_time(5)
#>>> google.pay_all_salary()   #nic nie wyplaci bo brak gościa
#>>> google_add_employee(employee2)
#google.pay_all_salary()
#1000

class Company:
    Company = "google"

    def __init__(self, nazwa, suma_wyplat, rozmiar_firmy):
        self.name = nazwa
        self.employees = set()
        self.salary_ammonut_all = suma_wyplat

        self.company_size = rozmiar_firmy

    def add_employee(self, employee):
        self.add_employee=set()

    def size(self):
        return len.self(employees)

    def pay_all_salary(self):
        sum_ = 0
        for e in self.employees:
           sum_ += e.pay_salary()

        return sum_

def test_company():
    employee = Employee('Jan', 'Nowak', 1000.0)
    employee.register_time(5)
    google = Company('google')
    google.add_employee(employee)
    assert google.size() == 1
    assert google.pay_all_salary()==0
    employee2 = Employee('Krzysztof', 'Nowak', 200.0)
    employee2.register_time(5)
    employee2.register_time(10)
    #google.pay_all_salary()   #nic nie wyplaci bo brak gościa
    google_add_employee(employee2)
    assert google.pay_all_salary()== 2200

    # google = Company('google')
    # assert google.name == 'google'

def test_add_employee():
    assert add_employee


# def test_
#employee = Emloyee()
