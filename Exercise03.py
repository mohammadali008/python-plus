#### I.N.O.G ---Collection of Exercise03-MohammadAli
import random
## --- Generate 10 Random numbers
random_index = [random.randint(1,50) for _ in range(10)]
print(random_index) # to get log
context = open('context.txt','r')
words = context.read().split()
for i in random_index:
    try:
        print(words[i])
    except errors:
        print('ok')
### --- Generate one float number between 10 to 20
print(random.uniform(10.0,20.0))


