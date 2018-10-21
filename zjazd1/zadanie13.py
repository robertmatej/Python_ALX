dni = int(input('dla ilu dni podajesz temperaturę: '))
# temp=int(input('podaj tepmeraturę dal dnia x'))
i = 1
suma = 0
min_=None   #pusta wartość ale nie 0
max_=None

# numer_dnia=0
while i <= dni:
    temp = int(input(f'podaj tepmeraturę dla dnia {i}: '))
    suma = suma + temp
    i += 1
    # numer_dnia+=1
# można znaleźć tmp min i max z okresu
'''  if i==1:
        min_=temp   
        max_=temp
    else:
        if temp<min_:
            min_=temp
        if
'''
print(i)

srednia = suma / (dni)
print(f'średnia temperatura z {dni} dni to {srednia}: ')
