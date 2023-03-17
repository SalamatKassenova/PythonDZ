#Задача 8: 

n = int(input('Введите количество долек по горизонтпли: '))
m = int(input('Введите количество долек по вертикали: '))
k = int(input('Сколько долек вы хотите получить за 1 разлом: '))

flag = True
if n<m:
    i=n
else:
    i=m
sum = int(n*m)
while flag:
    if k%i == 0 and k>=i:
        flag = False
        print('yes')
    else:
        print('no')
        flag = False