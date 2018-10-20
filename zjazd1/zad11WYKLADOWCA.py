pozx = int(input("podaj pozycję X gracza: "))
pozy = int(input ("podaj pozycję Y gracza: "))

rozmiar_plansza = 100
rx=100
ry=100
if pozx>rx or pozy>ry or pozx <0 or pozy <0:
    print ("wyszedłeś poza planszę, zacznij od nowa")
elif pozx>0.9*rx and pozy >0.9*ry:
    print("Jesteś w prawym górnym rogu planszy")
elif pozx>0.9*rx and pozy<0.1*ry:
    print("Jesteś w prawym dolnym rogu planszy")
elif pozx < 0.1*rx and pozy <0.1*ry:
    print("Jesteś w lewym dolnym rogu planszy")
elif pozx < 0.2*rx and pozy < 0.9*ry:
    print("Jesteś w lewym górnym rogu planszy")
elif pozx>90:
    print ("jestes na prawej krawedzi")
elif pozx < 10:
    print("jestes na prawej krawedzi")
elif pozy > 90:
    print("jestes u góry planszy")
elif pozy < 10:
    print("jestes na dole")


'''  
#prawa krawiędź
    if (pozx>0.9*rozmiar_plansza) and (pozy>0.9*rozmiar_plansza):
        print("Jesteś w prawym górnym rogu planszy")

    elif (pozx>0.9*rozmiar_plansza) and (pozy>0.1*rozmiar_plansza):
        print("Jesteś w prawym dolnym rogu planszy")

    elif (pozx > 0.9 * rozmiar_plansza) and (pozy > 0.1 * rozmiar_plansza) and (pozy < 0.9 * rozmiar_plansza):
        print("Jesteś na prawej krawędzi planszy")
#centrum Planszy
    elif (pozx < 0.9 * rozmiar_plansza) and (pozx > 0.1 * rozmiar_plansza) and (pozy > 0.1 * rozmiar_plansza) and (pozy < 0.9 * rozmiar_plansza):
        print("Jesteś w cetrum planszy")

#lewa krawędź
    elif (pozx < 0.1 * rozmiar_plansza) and (pozy > 0.9 * rozmiar_plansza):
        print("Jesteś w lewym górnym rogu planszy")

    elif (pozx < 0.1 * rozmiar_plansza) and (pozy < 0.1 * rozmiar_plansza):
        print("Jesteś w lewym dolnym rogu planszy")

    elif (pozx < 0.1 * rozmiar_plansza) and (pozy > 0.1 * rozmiar_plansza) and (pozy < 0.9 * rozmiar_plansza):
        print("Jesteś na lewej krawędzi planszy")

#dolna krawędź
    elif (pozx > 0.1 * rozmiar_plansza) and (pozy < 0.1 * rozmiar_plansza) and (pozx < 0.9 * rozmiar_plansza):
        print("Jesteś na dolnej krawędzi planszy")

#górna krawędź
    elif (pozx > 0.1 * rozmiar_plansza) and (pozx < 0.9 * rozmiar_plansza) and (pozy > 0.9 * rozmiar_plansza):
        print("Jesteś w górnej krawędzi planszy")

'''

