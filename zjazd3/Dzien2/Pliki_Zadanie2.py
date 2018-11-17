with open('../dane/logs.txt') as f:    # kropki cofają do do katalogu wyżej a pozniej wchodzę do własciwego folderu
    login = dict()
    iter = 0
    for a in f:
        user,status,time = f.split(';')
        login[iter] = a[1]
        iter+=1
    #print (f.read())
    print (f'dane: {login}')