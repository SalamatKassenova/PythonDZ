from random import randint, choice

import random

n = int(input('Введите количество монет: '))
sum1 = 0
sum2 = 0
for _ in range(n):
    k = random.randint(0, 1) # decide on a k each time the loop runs
    print(k, end = " ")
    if k == 1:
        sum1 = sum1 + 1
    else:
        sum2 = sum2 + 1
if sum1>sum2:
    print("\n")
    print(sum2)
else:
    print("\n")
    print(sum1)
