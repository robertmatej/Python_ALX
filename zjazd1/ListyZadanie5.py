
#    0   1   2   3

#y=range(1,999,75)
x=range(0,100)
y=range(0,1)
print
#for x in range(10):    #tu będize od zera
for x in range(1,10):
    print(f'{x:3}',end="")
print()
print()
#for x in range(10):    #tu będize od zera
for x in range(1,10):
    print(x, end="")
    for y in range(1,10):
        print(f"{x*y:3}",end="")

    print()

  #  range()