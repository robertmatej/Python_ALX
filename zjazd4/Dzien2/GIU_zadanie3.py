import tkinter

def sumuj():
    spalanie = float(spalanie_entry.get())       #metoda get() wyszukoje w całej przestrzeni nazw progermu nawet ponizej
    cena = float(cena_entry.get())
    dystans = float(dystans_entry.get())
    wynik.configure(text=(spalanie*dystans)*cena/100)                   # configura formatuje text? prezentuje w miejscu

root = tkinter.Tk()
#root.columnconfigure()                      #do ustalania wielkości pól

#spalanie
spalanie_label = tkinter.Label(master=root, text='Spalanie')
spalanie_label.grid(row=0,column=0)             # robimy wyświetlanie jak w siatce podajemy polozenie kolumny i wiersza

spalanie_entry = tkinter.Entry(master=root)
spalanie_entry.grid(row=0,column=1)

#cena
cena_label = tkinter.Label(master=root, text='Cena')
cena_label.grid(row=1,column=0)

cena_entry = tkinter.Entry(master=root)
cena_entry.grid(row=1,column=1)

#dystans
dystans_label = tkinter.Label(master=root, text='Dystans')
dystans_label.grid(row=2,column=0)

dystans_entry = tkinter.Entry(master=root)
dystans_entry.grid(row=2,column=1)


wynik_label = tkinter.Label(master=root, text='Koszt przejazdu PLN')
wynik_label.grid(row=3,column=0)
wynik = tkinter.Label(master=root, text='  ')
wynik.grid(row=3,column=1)


policz_button = tkinter.Button(master = root, text='Policz',command = sumuj)  #ostatni to wywolanie fuinkcji
policz_button.grid(row=4,column=0)


root.title('Kalkulator kosztów przejazdu')


# MAIN
root.mainloop()                 #pętla działająca do momenctu zamknięcia programu

print("ala ma kota")               # pojawi się dopiero po zamknieciu main loop, zam