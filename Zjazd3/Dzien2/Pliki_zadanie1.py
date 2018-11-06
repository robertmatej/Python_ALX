import sys
# wpisujemy w terminalu nazwe ppliku z programem poprzedazjac python

if len(sys.argv)>1:
    nazwa_pliku = sys.argv[1]

    with open(nazwa_pliku) as f:
       for i, line in enumerate(f,start =1):
            print(i, line, end="")

else:
    print("podaj nazwę pliuku: ")
