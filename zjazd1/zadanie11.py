pozx = int(input("podaj pozycję X gracza: "))
pozy = int(input ("podaj pozycję Y gracza: "))

rozmiar_plansza = 100

if pozx>100 or pozy>100:
    print ("wyszedłeś poza planszę, zacznij od nowa")
else:
    #prawa grawiedz
    if (pozx>0.9*rozmiar_plansza) and (pozy>0.9*rozmiar_plansza):
        print("Jesteś w prawym górnym rogu planszy")
    elif (pozx>0.9*rozmiar_plansza) and (pozy>0.1*rozmiar_plansza):
        print("Jesteś w prawym dolnym rogu planszy")
    elif (pozx > 0.9 * rozmiar_plansza) and (pozy > 0.1 * rozmiar_plansza):
        print("Jesteś w prawym dolnym rogu planszy")
    elif (pozx > 0.9 * rozmiar_plansza) and (pozy > 0.1 * rozmiar_plansza) and (pozy < 0.9 * rozmiar_plansza):
        print("Jesteś na prawej krawędzi planszy")

    elif (pozx < 0.9 * rozmiar_plansza) and (pozx > 0.1 * rozmiar_plansza) and (pozy > 0.1 * rozmiar_plansza) and (pozy < 0.9 * rozmiar_plansza):
        print("Jesteś w cetrum planszy")