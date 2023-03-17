#Задача 8: 

n = int(input('Введите количество долек по горизонтпли: '))
m = int(input('Введите количество долек по вертикали: '))
k = int(input('Сколько долек вы хотите получить за 1 разлом: '))

flag = True
if n<m:
    i=n
    x=m
else:
    i=m
    x=n
sum = int(n*m)
while flag:
    if (k%i == 0 and k>=i) or (k%x == 0 and k>=x):
        flag = False
        print('yes')
    else:
        print('no')
        flag = False