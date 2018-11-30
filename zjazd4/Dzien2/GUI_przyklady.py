import tkinter


def sumuj():
    a = float(a_entry.get())                    #metoda get() wyszukoje w całej przestrzeni nazw progermu nawet ponizej
    b = float(b_entry.get())
    wynik.configure(text=a+b)                   # configura formatuje text? prezentuje w miejscu

root = tkinter.Tk()             #przypmniemy różne funkcje
#Parametr a
a_label = tkinter.Label(master=root, text='Parametr a')
a_label.pack()
print (type(a_label))
a_entry = tkinter.Entry(master = root)
a_entry.pack()                          # powoduje pojawienie sę w oknie powyższej funkcji

# Parametr b
b_label = tkinter.Label(master=root, text='Parametr b')
b_label.pack()
b_entry = tkinter.Entry(master = root)
b_entry.pack()                          # powoduje pojawienie sę w oknie powyższej funkcji


wynik_label = tkinter.Label(master=root, text='Wynik')
wynik_label.pack()
wynik= tkinter.Label(master=root, text=' - ')
wynik.pack()


policz_button = tkinter.Button(master = root, text='Policz',command = sumuj)  #ostatni to wywolanie fuinkcji
policz_button.pack()



root.title('Sumator')



# MAIN
root.mainloop()                 #pętla działająca do momenctu zamknięcia programu

print("ala ma kota")               # pojawi się dopiero po zamknieciu main loop, zamkniecie okna