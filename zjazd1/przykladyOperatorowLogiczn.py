a = int(input("Podaj a"))
b = int(input("Podaj b"))
# b = 3

# a wieksze od b i a podzielne przez b
print("wynik ", a > b and a % b == 0)

# a wieksze od b lub a wieksze od 7
print("wynik 2 ", a > b or a > 7)

print("wynik 3", not a < 10)

if a > b and a == b:
    print(f"liczba {a} jest rowna {b} i jest podzilna przez {b}")
elif a==b:
    print(f"liczba a jest rowna b i wynosi {a}")
else:
    print("hahaha")

print("bbb")
