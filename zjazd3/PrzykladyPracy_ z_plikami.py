import csv

with open('dane/excell.csv',) as f:
    print(f.read())


with open('dane/nowy_plik.txt','w', encoding='utf8' ) as f:
    f.write("takie tam pisanie\n")

with open('dane/excell.csv',) as f:
    for line in f:
        print(line.upper(), end="")

with open('dane/logs.txt') as f:
    reader=csv.DictReader(f,delimiter=';')
    print(line)