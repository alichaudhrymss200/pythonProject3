import random
random.seed(10)
for i in range (10):
    print (random.randint(1,6),end="")

print ("reseeded")

random.seed(10)
for i in range (10):
    print(random.randint(1, 6), end="")

