# podajemy 2 liczby program ma dokonać jakiejś operacji matemeycznej (+ - dziel mnoż)
# podjamey tez operację w ,wyniku zlej operacji wyrzyca blad

liczba1 = float(input("Podaj liczbe A"))
liczba2 = float(input("Podaj liczbe B"))
operacja = input("Podaj jaką operację chcesz wykonać: mnożenie, dzlenia, dodawanie, odejmowanie ")


if operacja=="+":
    print (f"wynik dodawania liczb {liczba1} i {liczba2} wynosi {liczba1 + liczba2}")
elif operacja=="/":
    if liczba2 ==0:
        print("liczba 2 dne może być zerem podczas dzielenia")
    else:
            print (f"wynik dodawania liczb {liczba1} i {liczba2} wynosi {liczba1 / liczba2}")
            raise ValueError("NIE WOLNO DIZELIC przez ZERO2")
elif operacja=="-":
    print (f"wynik dodawania liczb {liczba1} i {liczba2} wynosi {liczba1 - liczba2}")
elif operacja=="*":
    print (f"wynik dodawania liczb {liczba1} i {liczba2} wynosi {liczba1 * liczba2}")
elif operacja =="l":
    pass   #pozwala zostaawić miejsce na przyszlosc
else:
    print ("podaleś niewłaściwe działanie proszę użyć działań w formacie +, - * , /")
    raise ValueError("nieprawidłowa wartość dla parametru typ operacja")


#zamiast tego mozna print na koniec a petli tylko operacje