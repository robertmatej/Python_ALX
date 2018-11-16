'''
Napisz program "lotto.py", który wyświetli 6 losowych i nie powtarzających się liczb z zakresu od 1 do 49.
'''
import random
#los = random.randint(1,49)
losuj = list()
i=0
while i<7:
    losuj.append(random.randint(1, 49))
#    print (losuj)
    i+=1
losowanie2 =random.sample(range(1,49), k = 6)


print(losuj)
wylosowane = random.sample(losuj, k=6)
print(wylosowane)
print(f'W dzisijeszym losowaniu wygrywają numery: {losowanie2}')