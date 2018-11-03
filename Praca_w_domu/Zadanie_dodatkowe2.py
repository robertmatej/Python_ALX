
tekst_wejsciowy = input('Podaj tekst do wypowiedzenia dla jąkały: ')
iteracja = 0
iteracja_wewnatrz = 0
tekst_wyjscie = list(tekst_wejsciowy)


for znak in tekst_wejsciowy:

    if (iteracja %2)!=0:
        #del tekst_wyjscie[iteracja]
        tekst_wyjscie.insert((iteracja+iteracja_wewnatrz), znak)
        iteracja_wewnatrz +=1

    iteracja += 1

print(''.join(tekst_wyjscie))
print(f"tekst po transformacji: {''.join(tekst_wyjscie)}")