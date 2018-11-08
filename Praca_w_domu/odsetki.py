'''
Napisz program "odsetki.py", który obliczy stan konta za N lat,
gdzie stan początkowy konta wynosi SPK, a stopa oprocentowania P %
rocznie (obowiązuje roczna kapitalizacja odsetek).
N, SPK i P podaje użytkownik programu.
'''
import sys


kapital_poczatkowy = int(sys.argv[1])
stopa_opr = float(sys.argv[2])
n_lat = int(sys.argv[3])


odsetki = int(kapital_poczatkowy*((1+stopa_opr*0.01)**n_lat))
podatek = 0.18*odsetki
odsetki_po_opodatkowaniu = odsetki-podatek
print (kapital_poczatkowy)
print (f'Twoje konto po {n_lat} latach, przy stopie procentowej: {stopa_opr} '
       f'i wkładzie początkowym: {kapital_poczatkowy} będzie wyglądało tak:  {odsetki_po_opodatkowaniu}. Państwo okradło cię na {podatek} ')

#źle liczy ale spełnia funkcjonalność