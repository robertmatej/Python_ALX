import json
import urllib.request
import tkinter
from collections import namedtuple

Weather = namedtuple('Weather', ['lokalizacja', 'temperatura', 'cisnienie', 'wilgotnosc', 'predkosc_wiatru'])

def pobranie_lokalizacji(szukaj_miasto):

 #   szukaj_miasto = str(input("Podaj nazwę miasta gdzie sprawdzisz pogodę: "))
    # if szukaj_miasto == None:
#    szukaj_miasto = "wars"

    woeid = None
    url_lokalizacja = f"https://www.metaweather.com/api/location/search/?query={szukaj_miasto}"
    with urllib.request.urlopen(url_lokalizacja) as f:
        location_data = json.load(f)
        for a in location_data:
            #if a["woeid"]:
            woeid = a['woeid']
            nazwa_miasta = a["title"]
            print (f"Lokalizacja: {nazwa_miasta}, kod: {woeid}")

    return woeid, nazwa_miasta

def pobranie_pogody(miasto):
    lokalizacja = int(pobranie_lokalizacji(miasto)[0])                      # funkcja zwraca tuple 2 wymiarową, wiec wybieram 1 element
    print (f"lokalizacja w pobraniu pog. {lokalizacja}")

    url_pogoda = f"https://www.metaweather.com/api/location/{lokalizacja}/"
    with urllib.request.urlopen(url_pogoda) as f:
        location_weather = json.load(f)
        # print (type(location_weather))
        # print ((location_weather))
        temp = (location_weather['consolidated_weather'][0]['the_temp'])
        lokalizacja = pobranie_lokalizacji(miasto)[1]
        cisnienie = location_weather['consolidated_weather'][0]['air_pressure']
        wilgotnosc = location_weather['consolidated_weather'][0]['humidity']
        predkosc_wiatru = location_weather['consolidated_weather'][0]['wind_speed']
        pogoda = Weather(lokalizacja , temp , cisnienie , wilgotnosc , predkosc_wiatru )

        return pogoda

def sprawdz_pogode():
    miasto = str(wprowadz_entry.get())
    pogoda = pobranie_pogody(miasto)
    print(pogoda)
    wynik = print(f'''Pogoda w {pogoda.lokalizacja}: 
          Temperatuira: {pogoda.temperatura}
          Ciśnienie: {pogoda.cisnienie}
          Wilgotność: {pogoda.wilgotnosc}
          Prędkość wiatru: {pogoda.predkosc_wiatru}
          
          ''')
    prognoza.configure(text=f'''Pogoda w {pogoda.lokalizacja}: 
          Temperatura: {pogoda.temperatura}
          Ciśnienie: {pogoda.cisnienie}
          Wilgotność: {pogoda.wilgotnosc}
          Prędkość wiatru: {pogoda.predkosc_wiatru}
          
          ''')
    #return pogoda, wynik


root = tkinter.Tk()
# wprowadzenie lokalizacji
wprowadz_label = tkinter.Label(master=root, text='Podaj lokalizację dla której sprwdzasz pogodę')
wprowadz_label.pack()
wprowadz_entry = tkinter.Entry(master = root)
wprowadz_entry.pack() # powoduje pojawienie sę w oknie powyższej funkcji


sprawdz_button = tkinter.Button(master = root, text='Pobierz POGODĘ', command = sprawdz_pogode)  # wywoluje funkcję
sprawdz_button.pack()

#wyniki wyszukania pogody
wynik_label = tkinter.Label(master=root, text='Aktualna Prognoza')
wynik_label.pack()
prognoza= tkinter.Label(master=root, text=f' :) ')
prognoza.pack()

root.title ("Prognoza pogody")

root.mainloop()
print("Winter's comming.. ")