import random

random.seed(3)   # ustala punkt względem czego jest losowanie wtedy jest powtażalne

print(random)
print(random.random())
print(random.randrange(1,100))
print(random.randint(1,100))


pets = ["cat", "dog", "fish", "kuna"]


print(random.choice(pets))


