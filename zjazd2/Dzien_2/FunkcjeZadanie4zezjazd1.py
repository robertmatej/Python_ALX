def zakupy (cena_za_kg, waga):

    naleznosc = waga*cena_za_kg
    return naleznosc

def wydruk(cena_za_kg, waga):
    naleznosc = waga * cena_za_kg
   # print(f'Należność za towar: {waga * cena_za_kg}')
    out=f"""cena za kilogram: {cena_za_kg}"
    Waga: {waga}
    Należność: {naleznosc}
    """
    return out


def test_zakupy():
    assert zakupy (10,2.4)==24

def test_drukuj():  #powinno zadziałać pwnie literóka
    assert test_drukuj(10, 2.4)==f"""cena za kilogram: {cena_za_kg}"
    Waga: {waga}
    Należność: {naleznosc}
    """