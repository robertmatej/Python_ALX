SAMOGLOSKI = 'aeiouy'
wyraz = input("podaj wyraz")
ile_samoglosek = 0
for znak in wyraz:
    if znak in SAMOGLOSKI:
        ile_samoglosek+=1

print (ile_samoglosek)
