# Napisz program, który wczyta od użytkownika tekst, a następnie wyświetli go w dwóch linijkach naprzemiennie,
# #
# #  np.: HELLO STRANGER! ->
# #
# # H L O S R N E !
# #
# #  E L   T A G R


tekst_wejsciowy = input(f'Podaj tekst do przerobienia: ')

linia_pierwsza = []
linia_druga = ['']

licznik_litery = 0

iteracja = 0
for znak in tekst_wejsciowy:

    if licznik_litery < len(tekst_wejsciowy) and (licznik_litery % 2) == 0:
        linia_pierwsza.append(znak)

    if licznik_litery < len(tekst_wejsciowy)and (licznik_litery % 2) != 0:
        linia_druga.append(znak)
    licznik_litery +=1


print(' '.join(linia_pierwsza))
print(' '.join(linia_druga))
