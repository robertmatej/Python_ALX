#na podstawie podanych wymiarow opakowania obliczyc objetosc i sprawdzic czy jest wieksza od 1litra 1000cm3

szer = int(input("ppdaj szerokos opakowania cm"))
gleb = int(input("ppdaj glebokosc opakowania cm"))
wys= int(input("ppdaj wzsokosc opakowania cm"))

poj=wys*szer*gleb

if poj>=1000:
    print("objetość ma litr lub więcej")
else:
    print("Pojemośc mniejsza od litra")

print (f"Pojemność opakowania wynosi {poj} cm3" )
