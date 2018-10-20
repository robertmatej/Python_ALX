zbior ={1,2,3,4,5,2,1}
zbior.add('a')
print(zbior)
print(11 in zbior)

for i in zbior:
        print(i)

a = {1,2,3}
b= {3,4,5}

print (a|b) #suma
print (a.union(b)) #suma

print (a - b) # roznica
print (a .difference(b)) # roznica

print (a & b) # czesc wspolna - iliczyn
print (a.intersection(b)) # czesc wspolna - iliczyn

print (a ^ b) # roznica symetryczna

print (dir(a))