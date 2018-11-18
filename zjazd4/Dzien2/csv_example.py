'''
Titanic ile osob umarlo ile pzezyło
policzyć przezywalność ppośrud ogulu, mężczyzn, kobiet
policzyć średnią wieku kobiet i mężczyzn


'''


import csv

wyniki = list()

with open ('c:/users/kurs/pycharmprojects/bootcamp/zjazd4/dane/titanic_train.csv') as f:
    data = csv.DictReader(f, delimiter=',')
    dlugosci = {}

    for row in data:
#        print(row)
        dlugosci[row['Survived']]= dlugosci.get(row['Survived'],0)+1



    #ogólem przezywalność
    przezylo= dlugosci['1']
    zginelo = dlugosci['0']
    print(f'przeżyło z ogółu {round(100*przezylo/(przezylo+zginelo),2)}%')



#kobietzy przeżyły
with open('c:/users/kurs/pycharmprojects/bootcamp/zjazd4/dane/titanic_train.csv') as f:
    data = csv.DictReader(f, delimiter=',')

    kobiety = {}
    for row in data:
        if row['Sex']=='female':
            kobiety[row['Survived']]= kobiety.get(row['Survived'],0)+1

    przezylo = kobiety['1']
    zginelo = kobiety['0']


    print(f'przeżyło kobiet {round(100*przezylo/(przezylo+zginelo),2)}%')

with open('c:/users/kurs/pycharmprojects/bootcamp/zjazd4/dane/titanic_train.csv') as f:
    data = csv.DictReader(f, delimiter=',')

    mezczyzni = {}
    for row in data:
        if row['Sex']=='female':
            mezczyzni[row['Survived']]= mezczyzni.get(row['Survived'],0)+1

    przezylo = mezczyzni['1']
    zginelo = mezczyzni['0']


    print(f'przeżyło mezczyzn {round(100*przezylo/(przezylo+zginelo),2)}%')

# średnia wieku przezywalnyego

with open('c:/users/kurs/pycharmprojects/bootcamp/zjazd4/dane/titanic_train.csv') as f:
    data = csv.DictReader(f, delimiter=',')

    how_many_woman = 0
    sum_woman_age = 0

    unique_age_values =set()
    for row in data:
        unique_age_values.add(row['Age'])  # potrzeowalismy do sprawdzeni wieku czy polowki czy cale
        if row['Sex']== 'female':
            how_many_woman += 1
            sum_woman_age += float(row['Age'])
        elif row['Sex']=='male':
            pass


    print(unique_age_values)
    print(f'Średnia wieku kobiet{sum_woman_age/how_many_woman}')

dane = ['ala ma kota', 'kot ma ale',['testowo', '2 gi poziom'],345 ]
# zapis do pliku !!!!!!!
with open("report.csv",'w')as f:
    writer = csv.writer(f)
    writer = writerows(dane)
