#Задача 6:

n = int(input('Введите шестизначный номер: '))
sum1 = 0
sum2 = 0
while n > 999:
    x = n%10
    sum1 = sum1 +x
    n = n//10

while n > 0 and n < 999:
    x = n%10
    sum2 = sum2 +x
    n = n//10

if sum1 == sum2:
    print('yes')
else:
    print('no')